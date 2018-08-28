include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPreInclude.py' )

splitConfig = runArgs.jobConfig[0].rstrip('.py').split('_')

#G/N2 degenerate
masses['1000022'] = float(splitConfig[5])  #--chi_10     LSP 
masses['1000023'] = float(splitConfig[4])  #--chi_20     NLSP

if masses['1000022']<0.5: 
  masses['1000022']=0.5

#will be WH
gentype = splitConfig[2]
#will be N2N2
decaytype = splitConfig[3]

decays['1000023'] = '''
#         PDG            Width
DECAY   1000023     1.09702033E-16   # neutralino2 decays
#          BR         NDA      ID1       ID2
     1.00000000E+00    2     1000022        22   # BR(~chi_2 -> gamma ~cHi-_1 )'''


process = '''
generate p p > h1 w+ , (w+ > l+ vl) @1 
add process p p > h1 w- , (w- > l- vl~) @1
'''
njets = 0
evgenLog.info('Registered generation of h1 w production, decay via  h > n2 n2, w > l vl; grid point '+str(runArgs.runNumber)+' decoded into mass point ' + str(masses['1000023']) + ' ' + str(masses['1000022']) )

evgenConfig.contact  = [ "haichen.wang@cern.ch" ]
evgenConfig.keywords += ['W', 'neutralino', 'lepton','longLived']
evgenConfig.description = 'h1 w production, decay via n2, n2 in simplified model, m_N1 = %s GeV, m_N2 = %s GeV'%(masses['1000022'],masses['1000023'])

#--------------------------------------------------------------
# add some filter here
#--------------------------------------------------------------

# need more events from MG due to filter - this needs to be set before MadGraphControl_SimplifiedModelPostInclude.py is run (it's set at 2 there)



include ( 'MC15JobOptions/MadGraphControl_SimplifiedModelPostInclude.py' )
testSeq.TestHepMC.MaxVtxDisp = 10000*10000 #in mm
testSeq.TestHepMC.MaxTransVtxDisp = 10000*10000
