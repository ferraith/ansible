#!powershell

# Copyright: (c) 2019, Andreas Schmidl <ferraith@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# WANT_JSON
# POWERSHELL_COMMON

Add-Type -AssemblyName System.IO.Compression.FileSystem

$ErrorActionPreference = "Stop"

$params = Parse-Args $args -supports_check_mode $true

$check_mode = Get-AnsibleParam -obj $params -name "_ansible_check_mode" -type "bool" -default $false
$path = Get-AnsibleParam -obj $params -name "path" -type "path" -failifempty $true
$format = Get-AnsibleParam -obj $params -name "format" -type "str" -default "zip" -ValidateSet "zip"
$dest = Get-AnsibleParam -obj $params -name "dest" -type "path" -default "$path.$format"
$compression_level = Get-AnsibleParam -obj $params -name "compression_level" -type "str" `
    -default "optimal" -ValidateSet "optimal","fastest","no_compression"

$compression_level_map = @{
    "optimal" = [System.IO.Compression.CompressionLevel] "Optimal";
    "fastest" = [System.IO.Compression.CompressionLevel] "Fastest";
    "no_compression" = [System.IO.Compression.CompressionLevel]  "NoCompression";
}

$result = @{
    changed = $false
    # remove trailing backslashes to prevent bad formatted JSON strings
    src = $path  -replace "\$",""
    dest = $dest  -replace "\$",""
}

if ($format -eq "zip") {
    if (-not $check_mode) {
        try {
            [System.IO.Compression.ZipFile]::CreateFromDirectory(
                $path,
                $dest,
                $compression_level_map[$compression_level],
                $false
            );
        } catch {
            Fail-Json -obj $result `
                -message "Error archiving '$path' to '$dest': $($_.Exception.Message)"
        }
        $result.changed = $true
    }
}

Exit-Json $result
