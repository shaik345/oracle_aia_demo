import sys

domain_home='{{domain_home}}'
aia_template=fmw_home + '/soa/common/templates/wls/oracle.soa.fp_template.jar'
readDomain(domain_home)
addTemplate(aia_template)
updateDomain(domain_configuration_home)
closeDomain()
