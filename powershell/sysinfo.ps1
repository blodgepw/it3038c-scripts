
$Hello = "Hello, PowerShell"
Write-Host($Hello)
function getIP {
(Get-NetIPAddress).IPv4Address | select-string "192*"
}

write-host(getIP)
$IP = getIP
Write-host("This machine's IP is $IP")
Write-host("This machine's IP is {0}" -f $IP)