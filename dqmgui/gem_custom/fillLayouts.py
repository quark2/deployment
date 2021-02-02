import os, sys, re, argparse


listDictLayers = [
    { "re": -1, "st": 1, "la": 1, "ch": 36, "ie":  8 }, 
    { "re": -1, "st": 1, "la": 2, "ch": 36, "ie":  8 }, 
    { "re":  1, "st": 1, "la": 1, "ch": 36, "ie":  8 }, 
    { "re":  1, "st": 1, "la": 2, "ch": 36, "ie":  8 }, 
  ]

strFmtId   = "GE%(re)+i%(st)iL%(la)i"
strFmtPath = "re%(re)i_st%(st)i_la%(la)i"
strFmtDesc = "in GE%(re)+i/%(st)i Layer %(la)i"

strFmtChId   = " Chamber %02i"
strFmtChPath = "_ch%02i"
strFmtChDesc = "Chamber %02i"


nIdx = 0
listItemLayout = []
listItemWS     = []


def ConstructListItems(): 
  global nIdx
  nIdx = 0
  
  def wIdx(s): 
    global nIdx
    nIdx += 1
    return s%(nIdx - 1)
  
  def AddItem(l, name, *rows): l.append({ "name": name, "rows": rows })
  
  AddItem(listItemLayout, wIdx("Common/%02i Summary"), 
      [{"path" : "GEM/EventInfo/reportSummaryMap", 
        "description": 'For more information (... under construction)'}])
  listItemWS.append(listItemLayout[ -1 ][ "name" ])
  
  AddItem(listItemLayout, wIdx("Common/%02i AMC status positive endcap"), 
      [{"path" : "GEM/DAQStatus/amc_statusflagPos", 
        "description": 'For more information (... under construction)'}])
  listItemWS.append(listItemLayout[ -1 ][ "name" ])
  
  AddItem(listItemLayout, wIdx("Common/%02i AMC status negative endcap"), 
      [{"path" : "GEM/DAQStatus/amc_statusflagNeg", 
        "description": 'For more information (... under construction)'}])
  listItemWS.append(listItemLayout[ -1 ][ "name" ])
  
  for d in listDictLayers: 
    strKeyId, strKeyPath, strKeyDesc = (strFmtId%d, strFmtPath%d, strFmtDesc%d)
    AddItem(listItemLayout, wIdx("Common/%02i " + strKeyId + " GEB input status"), 
        [{"path": "GEM/DAQStatus/geb_input_status_" + strKeyPath, 
          "description": "GEB input status " + strKeyDesc}, 
        ])
    listItemWS.append(listItemLayout[ -1 ][ "name" ])
  
  for d in listDictLayers: 
    strKeyId, strKeyPath, strKeyDesc = (strFmtId%d, strFmtPath%d, strFmtDesc%d)
    AddItem(listItemLayout, wIdx("Common/%02i " + strKeyId + " VFAT input status"), 
        [{"path": "GEM/DAQStatus/vfat_status_" + strKeyPath, 
          "description": "VFAT input status " + strKeyDesc}, 
        ])
    listItemWS.append(listItemLayout[ -1 ][ "name" ])
  
  for d in listDictLayers: 
    strKeyId, strKeyPath, strKeyDesc = (strFmtId%d, strFmtPath%d, strFmtDesc%d)
    AddItem(listItemLayout, wIdx("Common/%02i " + strKeyId + " bunch crossing"), 
        [{"path": "GEM/digi/bx_" + strKeyPath, 
          "description": "Bunch crossing " + strKeyDesc}, 
        ])
    listItemWS.append(listItemLayout[ -1 ][ "name" ])
  
  for d in listDictLayers: 
    strKeyId, strKeyPath, strKeyDesc = (strFmtId%d, strFmtPath%d, strFmtDesc%d)
    AddItem(listItemLayout, wIdx("Common/%02i " + strKeyId + " digi occupancy"), 
        [{"path": "GEM/digi/digi_det_" + strKeyPath, 
          "description": "Digi occupancy " + strKeyDesc}, 
        ])
    listItemWS.append(listItemLayout[ -1 ][ "name" ])
  
  for d in listDictLayers: 
    strKeyId, strKeyPath, strKeyDesc = (strFmtId%d, strFmtPath%d, strFmtDesc%d)
    AddItem(listItemLayout, wIdx("Common/%02i " + strKeyId + " digi occupancy vs iEta"), 
        [{"path": "GEM/digi/strip_ieta_occ_" + strKeyPath, 
          "description": "Digi occupancy vs iEta " + strKeyDesc}, 
        ])
    listItemWS.append(listItemLayout[ -1 ][ "name" ])
  
  for d in listDictLayers: 
    strKeyId, strKeyPath, strKeyDesc = (strFmtId%d, strFmtPath%d, strFmtDesc%d)
    AddItem(listItemLayout, wIdx("Common/%02i " + strKeyId + " digi occupancy vs phi"), 
        [{"path": "GEM/digi/strip_phi_occ_" + strKeyPath, 
          "description": "Digi occupancy vs phi " + strKeyDesc}, 
        ])
    listItemWS.append(listItemLayout[ -1 ][ "name" ])
  
  for d in listDictLayers: 
    strKeyId, strKeyPath, strKeyDesc = (strFmtId%d, strFmtPath%d, strFmtDesc%d)
    AddItem(listItemLayout, wIdx("Common/%02i " + strKeyId + " total number of strips per event"), 
        [{"path": "GEM/digi/total_strips_per_event_" + strKeyPath, 
          "description": "Total number of strips per event " + strKeyDesc}, 
        ])
    listItemWS.append(listItemLayout[ -1 ][ "name" ])
  
  for d in listDictLayers: 
    strKeyId, strKeyPath, strKeyDesc = (strFmtId%d, strFmtPath%d, strFmtDesc%d)
    AddItem(listItemLayout, wIdx("Common/%02i " + strKeyId + " recHit occupancy"), 
        [{"path": "GEM/recHit/rechit_det_" + strKeyPath, 
          "description": "recHit occupancy " + strKeyDesc}, 
        ])
    listItemWS.append(listItemLayout[ -1 ][ "name" ])
  
  for d in listDictLayers: 
    strKeyId, strKeyPath, strKeyDesc = (strFmtId%d, strFmtPath%d, strFmtDesc%d)
    AddItem(listItemLayout, wIdx("Common/%02i " + strKeyId + " recHit occupancy vs iEta"), 
        [{"path": "GEM/recHit/rechit_ieta_occ_" + strKeyPath, 
          "description": "recHit occupancy vs iEta " + strKeyDesc}, 
        ])
    listItemWS.append(listItemLayout[ -1 ][ "name" ])
  
  for d in listDictLayers: 
    strKeyId, strKeyPath, strKeyDesc = (strFmtId%d, strFmtPath%d, strFmtDesc%d)
    AddItem(listItemLayout, wIdx("Common/%02i " + strKeyId + " recHit occupancy vs phi"), 
        [{"path": "GEM/recHit/rechit_phi_occ_" + strKeyPath, 
          "description": "recHit occupancy vs phi " + strKeyDesc}, 
        ])
    listItemWS.append(listItemLayout[ -1 ][ "name" ])
  
  for d in listDictLayers: 
    strKeyId, strKeyPath, strKeyDesc = (strFmtId%d, strFmtPath%d, strFmtDesc%d)
    AddItem(listItemLayout, wIdx("Common/%02i " + strKeyId + " total number of recHits per event"), 
        [{"path": "GEM/recHit/total_rechit_per_event_" + strKeyPath, 
          "description": "Total number of recHits per event " + strKeyDesc}, 
        ])
    listItemWS.append(listItemLayout[ -1 ][ "name" ])
  
  for d in listDictLayers: 
    for ie in range(1, d[ "ie" ] + 1): 
      strKeyId, strKeyPath, strKeyDesc = (strFmtId%d, strFmtPath%d, strFmtDesc%d)
      strKeyId   += " iEta %i"%ie
      strKeyPath += "_ieta%02i"%ie
      strKeyDesc += " iEta %i"%ie
      AddItem(listItemLayout, wIdx("Common/%02i " + strKeyId + " cluster size"), 
          [{"path": "GEM/recHit/cls_" + strKeyPath, 
            "description": "Cluster size distribution " + strKeyDesc}, 
          ])
      listItemWS.append(listItemLayout[ -1 ][ "name" ])
  
  #for layer in listLayersWithTitle: 
  #  AddItem(listItemLayout, "Common/%02i Global position %s"%(nIdx, layer[ 1 ]), 
  #      [{"path": "GEM/recHit/recHit_globalPos_Gemini_GE" + layer[ 0 ], 
  #        "description": "Global position"}])
  #  nIdx += 1
  
  for d in listDictLayers: 
    nIdx = 0
    for ch in range(1, d[ "ch" ] + 1): 
      strKeyId, strKeyPath, strKeyDesc = (strFmtId%d, strFmtPath%d, strFmtDesc%d)
      strKeyId   += " Chamber %02i"%ch
      strKeyPath += "_ch%02i"%ch
      strKeyDesc += " Chamber %02i"%ch
      strDirLayout = "GE%(re)+i%(st)i L%(la)i"%d
      
      AddItem(listItemLayout, wIdx(strDirLayout + "/%02i " + strKeyId), 
        [
          {"path": "GEM/DAQStatus/vfat_status_" + strKeyPath, 
           "description": "VFAT status"},
          {"path": "GEM/digi/bx_ch_"            + strKeyPath, 
           "description": "Bunch crossing"},
        ],
        [
          {"path": "GEM/digi/strip_occ_"        + strKeyPath, 
           "description": "Digi occupancy"},
          {"path": "GEM/recHit/cls_"            + strKeyPath, 
           "description": "VFAT vs ClusterSize"},
        ]
      )


def AddItemToLayout(strCodeLayout, listLayout): 
  strHead  = "# Generated by dqmgui/gem_custom/fillLayouts.py \n"
  strHead += "#   in https://github.com/quark2/deployment/tree/addingGem\n"
  strHead += """def GEMLayout(i, p, *rows): i["GEM/Layouts/" + p] = DQMItem(layout=rows)"""
  
  strFmtLayout = """GEMLayout(dqmitems, '%(name)s', 
%(rows)s
    )"""
  
  listLines = [ strHead, "" ]
  
  for dicItem in listLayout: 
    strRows = "\n".join([ "    {}, ".format(l) for l in dicItem[ "rows" ] ])
    listLines.append(strFmtLayout%{"name": dicItem[ "name" ], "rows": strRows})
  
  with open(strCodeLayout, "w") as fOut: fOut.write("\n".join(listLines))


def AddItemToWS(strCodeWorkspace, listWS): 
  strServerWorkspaceBegin  = "# Generated by dqmgui/gem_custom/fillLayouts.py \n"
  strServerWorkspaceBegin += "#   in https://github.com/quark2/deployment/tree/addingGem\n"
  strServerWorkspaceBegin += "server.workspace('DQMContent', 43, 'Muons', 'GEM', '^GEM/', '',"
  strServerWorkspaceEnd    = "                )"
  
  # Creating the lines for GEM
  listLinesGEM = []
  listLinesGEM.append(strServerWorkspaceBegin)
  for strName in listWS: 
    listLinesGEM.append(" " * len(strServerWorkspaceEnd) + "'GEM/Layouts/%s', "%strName)
  listLinesGEM.append(strServerWorkspaceEnd)
  #strLinesGEM = "\n".join(listLinesGEM)
  
  # Analysing and decomposing the existing file
  listLinesWS = []
  with open(strCodeWorkspace) as fExist: listLinesWS += fExist.read().splitlines()
  
  listLinesNewWS = []
  reWSRegion = re.compile("^#[ ]*(?P<region>[\w]+) workspaces:")
  bAdding = True
  for strLine in listLinesWS: 
    reRes = reWSRegion.match(strLine)
    if reRes == None and bAdding: listLinesNewWS.append(strLine)
    elif reRes != None: 
      if reRes.groupdict()[ "region" ] != "GEM": 
        listLinesNewWS.append(strLine)
        bAdding = True
      else: 
        listLinesNewWS.append(strLine)
        bAdding = False
        listLinesNewWS += listLinesGEM + [ "" ]
  
  with open(strCodeWorkspace, "w") as fOut: fOut.write("\n".join(listLinesNewWS))


def doMain(): 
  class oo(object): pass
  opts = oo()
  opts.strFileLayout = "layouts/gem-layouts.py"
  opts.strFileWS     = "workspaces-online.py"
  
  ConstructListItems()
  AddItemToLayout(opts.strFileLayout, listItemLayout)
  AddItemToWS(opts.strFileWS, listItemWS)


if __name__ == "__main__": 
  doMain()


