### RPM cms cmssw CMSSW_0_8_0_pre5
## IMPORT configurations
Provides: /bin/zsh
Requires: cmssw-tool-conf python
%define toolconf ${CMSSW_TOOL_CONF_ROOT}/configurations/tools-STANDALONE.conf
%define cvsdir %(echo %n | tr 'a-z' 'A-Z')
%define cvsserver %(echo %n | tr 'A-Z' 'a-z')
%define patchsrc perl -p -i -e 's!<select name=(MyODBC|ignominy|rulechecker)>!!' config/requirements ;
#%define patchsrc2 perl -p -i -e 's|INCLUDE(.*root/cint">)$|CINT_INCLUDE$1|' SCRAMToolBox/General/ROOTCore SCRAMToolBox/CMS/Tools/ROOTCore
%define confversion %cmsConfiguration
%define conflevel   _2
%define preBuildCommand (rm -rf SimMuon/DTDigitizer/test)
%define buildtarget release-build 
## IMPORT cms-scram-build
## IMPORT scramv1-build

