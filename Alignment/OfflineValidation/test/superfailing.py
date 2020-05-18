>>>>>>>>>> testPVValidation_cfg.py: msg%-i: This is real DATA!
>>>>>>>>>> testPVValidation_cfg.py: msg%-i: JSON filtering with: None 
>>>>>>>>>> testPVValidation_cfg.py: msg%-i: Running DA Algorithm!
Done
import FWCore.ParameterSet.Config as cms

process = cms.Process("PrimaryVertexValidation")

process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string('checkAllFilesOpened'),
    fileNames = cms.untracked.vstring('/store/express/Run2018C/StreamExpress/ALCARECO/TkAlMinBias-Express-v1/000/319/347/00000/E230C5AB-1383-E811-BB27-FA163EA114BD.root'),
    firstRun = cms.untracked.uint32(319347),
    lumisToProcess = cms.untracked.VLuminosityBlockRange( (
        "314472:55-314472:89", "314473:1-314473:18", "314474:1-314474:18", "314475:1-314475:18", "314476:1-314476:17", 
        "314477:1-314477:17", "314478:1-314478:12", "314479:1-314479:12", "314480:1-314480:13", "314481:1-314481:13", 
        "314482:1-314482:12", "314483:1-314483:12", "314485:1-314485:13", "314486:1-314486:13", "314487:1-314487:15", 
        "314488:1-314488:13", "314490:1-314490:13", "314491:1-314491:13", "314492:1-314492:19", "314494:1-314494:22", 
        "314495:1-314495:14", "314496:1-314496:15", "314497:1-314497:12", "314498:1-314498:12", "314499:1-314499:13", 
        "314500:1-314500:12", "314501:1-314501:12", "314502:1-314502:12", "314503:1-314503:12", "314504:1-314504:12", 
        "314506:1-314506:17", "314507:1-314507:13", "314508:1-314508:14", "314509:1-314509:12", "314510:1-314510:12", 
        "314511:1-314511:14", "314512:1-314512:12", "314513:1-314513:12", "314515:1-314515:75", "314521:1-314521:7", 
        "314521:9-314521:48", "314524:1-314524:12", "314527:1-314527:13", "314557:1-314557:23", "314558:1-314558:36", 
        "314559:1-314559:11", "314560:1-314560:11", "314562:1-314562:11", "314563:1-314563:23", "314564:1-314564:25", 
        "314565:1-314565:26", "314566:1-314566:26", "314567:1-314567:27", "314568:1-314568:2", "314570:1-314570:25", 
        "314571:1-314571:27", "314572:1-314572:23", "314573:1-314573:23", "314574:1-314574:9", "314574:13-314574:339", 
        "314575:1-314575:25", "314649:37-314649:64", "314649:67-314649:76", "314649:78-314649:86", "314650:1-314650:23", 
        "314650:26-314650:54", "314650:56-314650:74", "314650:76-314650:84", "314650:86-314650:104", "314650:106-314650:114", 
        "314650:116-314650:145", "314650:147-314650:155", "314650:157-314650:165", "314650:167-314650:175", "314650:177-314650:186", 
        "314650:189-314650:287", "314650:289-314650:297", "314650:299-314650:318", "314650:320-314650:328", "314650:330-314650:340", 
        "314650:344-314650:412", "314650:414-314650:453", "314650:455-314650:473", "314650:475-314650:483", "314650:485-314650:495", 
        "314650:499-314650:537", "314650:539-314650:597", "314650:599-314650:608", "314650:610-314650:618", "314650:620-314650:638", 
        "314650:641-314650:649", "314650:652-314650:664", "314651:1-314651:6", "314652:1-314652:13", "314653:1-314653:12", 
        "314654:1-314654:12", "314655:1-314655:12", "314656:1-314656:12", "314657:1-314657:12", "314658:1-314658:12", 
        "314659:1-314659:12", "314660:1-314660:12", "314661:1-314661:11", "314662:1-314662:13", "314663:1", 
        "314663:5-314663:13", "314663:15-314663:24", "314663:26-314663:34", "314663:36-314663:44", "314663:46-314663:54", 
        "314663:57-314663:75", "314663:77-314663:85", "314663:87-314663:96", "314663:99-314663:127", "314663:129-314663:138", 
        "314663:141-314663:149", "314663:151-314663:160", "314663:162-314663:170", "314663:172-314663:181", "314663:184-314663:198", 
        "314663:201-314663:209", "314663:211-314663:219", "314663:221-314663:229", "314663:231-314663:240", "314663:242-314663:250", 
        "314663:252-314663:260", "314663:262-314663:270", "314663:272-314663:280", "314663:283-314663:291", "314663:293-314663:301", 
        "314663:303-314663:312", "314663:314-314663:322", "314663:325-314663:334", "314663:336-314663:344", "314663:346-314663:354", 
        "314663:356-314663:365", "314663:367-314663:375", "314663:377-314663:385", "314663:387-314663:395", "314663:397-314663:406", 
        "314663:408-314663:416", "314663:418-314663:447", "314663:449-314663:457", "314663:505-314663:526", "314664:1-314664:184", 
        "314665:1-314665:13", "314747:52-314747:62", "314748:1-314748:29", "314750:1-314750:9", "314751:1-314751:9", 
        "314752:1-314752:10", "314753:1-314753:2", "314754:1-314754:12", "314755:1-314755:61", "314755:65-314755:347", 
        "314755:349-314755:352", "314756:1-314756:211", "314758:1-314758:21", "314759:1-314759:680", "314764:1-314764:247", 
        "314810:12-314810:121", "314811:1-314811:784", "314816:33-314816:1082", "314859:22-314859:79", "314860:1-314860:55", 
        "314861:1-314861:16", "314863:1-314863:35", "314864:1-314864:48", "314865:1-314865:28", "314867:1-314867:48", 
        "314870:1-314870:29", "314872:1-314872:10", "314873:1-314873:34", "314874:1-314874:38", "314875:1-314875:151", 
        "314876:1-314876:43", "314878:1-314878:537", "314890:49-314890:1433", "315104:39-315104:266", "315105:1-315105:3", 
        "315106:1-315106:565", "315107:1-315107:455", "315108:1-315108:146", "315150:57-315150:122", "315151:1-315151:77", 
        "315154:1-315154:200", "315157:1-315157:17", "315159:1-315159:154", "315172:1-315172:318", "315179:33-315179:65", 
        "315180:1-315180:21", "315187:38-315187:43", "315188:1-315188:305", "315189:1-315189:383", "315190:1-315190:96", 
        "315257:1-315257:88", "315257:91-315257:92", "315258:1", "315259:1-315259:172", "315264:32-315264:261", 
        "315265:4-315265:58", "315267:1-315267:244", "315268:1-315268:3", "315270:1-315270:633", "315322:23-315322:118", 
        "315322:122-315322:1354", "315339:37-315339:654", "315357:44-315357:732", "315357:736-315357:770", "315357:780-315357:831", 
        "315361:40-315361:623", "315363:1-315363:136", "315365:1-315365:25", "315366:1-315366:750", "315420:28-315420:920", 
        "315420:924-315420:942", "315420:954-315420:1748", "315488:42-315488:1113", "315489:1-315489:709", "315490:1-315490:24", 
        "315506:13-315506:100", "315509:1-315509:53", "315510:1-315510:345", "315512:1-315512:1122", "315543:55-315543:171", 
        "315555:22-315555:97", "315556:1-315556:26", "315557:1-315557:279", "315640:46-315640:87", "315641:1-315641:4", 
        "315642:1-315642:92", "315644:1-315644:184", "315645:1-315645:594", "315646:1-315646:1033", "315647:1-315647:58", 
        "315648:1-315648:111", "315689:24-315689:1186", "315690:1-315690:654", "315702:38-315702:113", "315703:1-315703:545", 
        "315704:1-315704:62", "315705:1-315705:700", "315713:35-315713:1123", "315721:33-315721:626", "315741:34-315741:92", 
        "315764:37-315764:309", "315770:39-315770:332", "315784:29-315784:200", "315785:1-315785:198", "315785:201-315785:305", 
        "315786:1-315786:72", "315788:1-315788:3", "315789:1-315789:3", "315790:1-315790:922", "315800:41-315800:651", 
        "315801:1-315801:344", "315840:33-315840:1154", "315973:39-315973:914", "315974:1-315974:71", "316058:42-316058:405", 
        "316059:1-316059:567", "316060:1-316060:935", "316061:1-316061:23", "316061:194-316061:206", "316062:1-316062:4", 
        "316082:37-316082:407", "316109:34-316109:45", "316110:1-316110:210", "316111:1-316111:48", "316112:1-316112:9", 
        "316113:1-316113:68", "316114:1-316114:777", "316114:779-316114:1562", "316151:5", "316153:1-316153:770", 
        "316186:38-316186:81", "316187:1-316187:1091", "316187:1093-316187:1100", "316187:1207-316187:2077", "316199:33-316199:1197", 
        "316200:1-316200:10", "316201:1-316201:498", "316202:1-316202:403", "316216:25-316216:466", "316217:1-316217:264", 
        "316218:1-316218:1023", "316219:1-316219:283", "316239:38-316239:629", "316240:1-316240:1233", "316241:1-316241:325", 
        "316271:36-316271:122", "316361:22-316361:223", "316362:1-316362:450", "316363:1-316363:49", "316377:19-316377:40", 
        "316378:1-316378:29", "316379:1-316379:70", "316380:1-316380:1213", "316441:1-316441:6", "316455:36-316455:71", 
        "316456:1-316456:2", "316457:1-316457:1455", "316469:17-316469:645", "316470:1-316470:476", "316472:1-316472:333", 
        "316505:44-316505:1364", "316569:20-316569:1945", "316590:17-316590:526", "316613:49-316613:241", "316614:1-316614:2", 
        "316615:1-316615:338", "316664:1-316664:13", "316665:1-316665:247", "316666:1-316666:981", "316667:1-316667:197", 
        "316700:46-316700:346", "316700:388-316700:397", "316701:1-316701:479", "316702:1-316702:388", "316715:33-316715:74", 
        "316716:1-316716:181", "316717:1-316717:192", "316718:1-316718:348", "316719:1-316719:144", "316720:1-316720:182", 
        "316721:1-316721:27", "316722:1-316722:751", "316723:1-316723:64", "316758:11-316758:1609", "316766:51-316766:2199", 
        "316876:34-316876:654", "316877:1-316877:401", "316879:1-316879:156", "316928:40-316928:188", "316944:41-316944:1831", 
        "316985:33-316985:503", "316993:44-316993:254", "316994:1-316994:20", "316995:1-316995:623", "317080:41-317080:66", 
        "317087:43-317087:177", "317087:213-317087:222", "317087:257-317087:852", "317088:1-317088:25", "317089:1-317089:1003", 
        "317182:47-317182:1424", "317212:36-317212:175", "317213:1-317213:375", "317279:43-317279:508", "317291:34-317291:838", 
        "317292:1-317292:350", "317295:1-317295:19", "317296:1-317296:103", "317297:1-317297:760", "317319:44-317319:182", 
        "317320:1-317320:411", "317320:413-317320:1828", "317338:66-317338:107", "317339:1-317339:176", "317340:1-317340:418", 
        "317382:58-317382:128", "317383:1-317383:58", "317391:39-317391:46", "317392:1-317392:1900", "317434:48-317434:257", 
        "317435:1-317435:1397", "317438:1-317438:68", "317438:71-317438:309", "317475:33-317475:89", "317475:105-317475:115", 
        "317478:1-317478:23", "317479:1-317479:18", "317480:1-317480:14", "317481:1-317481:20", "317482:1-317482:25", 
        "317484:1-317484:448", "317484:467-317484:514", "317484:519-317484:545", "317488:1-317488:844", "317509:23-317509:353", 
        "317510:1-317510:11", "317511:1-317511:412", "317512:1-317512:443", "317527:41-317527:1487", "317591:43-317591:334", 
        "317626:40-317626:2045", "317640:29-317640:829", "317641:1-317641:1390", "317648:45-317648:139", "317649:1-317649:621", 
        "317650:1-317650:1304", "317661:35-317661:1336", "317663:1-317663:858", "317683:83-317683:402", "317696:38-317696:682", 
        "318733:1-318733:33", "318816:51-318816:210", "318819:1-318819:34", "318820:1-318820:65", "318828:54-318828:123", 
        "318872:16-318872:287", "318874:1-318874:320", "318876:1-318876:161", "318877:1-318877:615", "318944:1-318944:7", 
        "319077:52-319077:92", "319310:124-319310:125", "319337:48-319337:2240", "319347:40-319347:690", "319348:1-319348:37", 
        "319349:1-319349:148", "319449:35-319449:734", "319450:1-319450:683", "319456:138-319456:346", "319459:1-319459:78", 
        "319486:38-319486:103", "319503:1-319503:317", "319524:36-319524:1459", "319526:1-319526:282", "319527:1-319527:3", 
        "319528:1-319528:259", "319579:41-319579:3168", "319625:17-319625:206", "319639:31-319639:1509", "319656:51-319656:310", 
        "319657:1-319657:167", "319658:1-319658:225", "319659:1-319659:87", "319678:36-319678:294", "319687:46-319687:90", 
        "319697:47-319697:490", "319698:1-319698:312", "319756:44-319756:1966", "319840:41-319840:388", "319841:1-319841:167", 
        "319847:49-319847:51", "319848:1-319848:53", "319849:1-319849:492", "319851:1-319851:13", "319852:1-319852:9", 
        "319853:1-319853:262", "319854:1-319854:225", "319908:1-319908:53", "319909:1-319909:7", "319910:1-319910:989", 
        "319912:1-319912:62", "319913:1-319913:61", "319914:1-319914:37", "319915:1-319915:417", "319941:43-319941:305", 
        "319942:1-319942:51", "319950:38-319950:205", "319991:46-319991:886", "319992:1-319992:268", "319993:1-319993:955", 
        "320002:52-320002:193", "320006:1-320006:344", "320007:1-320007:161", "320008:1-320008:89", "320009:1-320009:127", 
        "320010:1-320010:333", "320011:1-320011:307", "320012:1-320012:100", "320023:17-320023:294", "320024:1-320024:410", 
        "320025:1-320025:113", "320026:1-320026:204", "320038:43-320038:668", "320039:1-320039:36", "320040:1-320040:738", 
        "320058:44-320058:71", "320059:1-320059:113", "320060:1-320060:50", "320061:1-320061:50", "320062:1-320062:24", 
        "320063:1-320063:76", "320064:1-320064:204", "320065:1-320065:921", "320500:127-320500:147", "320500:150-320500:158", 
        "320500:160-320500:168", "320500:170-320500:179", "320500:181-320500:189", "320500:191-320500:199", "320500:201-320500:209", 
        "320500:211-320500:230", "320500:232-320500:240", "320500:243-320500:251", "320500:253-320500:262", "320500:264-320500:273", 
        "320500:275-320500:284", "320500:286-320500:294", "320500:297-320500:304", "320500:306-320500:315", "320500:317-320500:318", 
        "320500:322-320500:350", "320500:352-320500:360", "320500:362-320500:415", "320500:417-320500:469", "320500:471-320500:478", 
        "320569:57-320569:307", "320570:1-320570:13", "320570:16-320570:35", "320570:37-320570:45", "320570:47-320570:115", 
        "320570:117-320570:135", "320570:137-320570:165", "320570:167-320570:175", "320570:177-320570:186", "320570:191-320570:199", 
        "320570:201-320570:229", "320570:231-320570:240", "320570:242-320570:363", "320570:365-320570:419", "320571:1-320571:63", 
        "320673:35-320673:906", "320674:1-320674:600", "320688:49-320688:648", "320712:39-320712:242", "320757:51-320757:383", 
        "320804:46-320804:1283", "320807:1-320807:11", "320809:1-320809:717", "320821:41-320821:225", "320822:1-320822:526", 
        "320823:1-320823:364", "320824:1-320824:1052", "320838:93-320838:358", "320839:1-320839:8", "320840:1-320840:474", 
        "320841:1-320841:206", "320853:41-320853:371", "320854:1-320854:126", "320855:1-320855:577", "320856:1-320856:164", 
        "320857:1-320857:277", "320858:1-320858:239", "320859:1-320859:41", "320887:49-320887:325", "320888:1-320888:124", 
        "320916:2-320916:25", "320917:1-320917:1926", "320920:1-320920:178", "320933:40-320933:214", "320934:1-320934:831", 
        "320936:1-320936:407", "320941:1-320941:93", "320980:44-320980:142", "320995:26-320995:214", "320996:1-320996:380", 
        "321004:39-321004:188", "321005:1-321005:61", "321006:1-321006:162", "321007:1-321007:831", "321009:1-321009:85", 
        "321010:1-321010:342", "321011:1-321011:213", "321012:1-321012:35", "321012:190-321012:201", "321051:58-321051:1179", 
        "321055:1-321055:759", "321067:39-321067:639", "321068:1-321068:715", "321069:1-321069:313", "321119:45-321119:214", 
        "321121:1-321121:47", "321122:1-321122:395", "321123:1-321123:8", "321124:1-321124:819", "321126:1-321126:493", 
        "321134:33-321134:137", "321138:1-321138:741", "321140:1-321140:798", "321149:35-321149:1743", "321162:19-321162:59", 
        "321164:1-321164:72", "321165:1-321165:8", "321166:1-321166:21", "321167:1-321167:923", "321177:38-321177:523", 
        "321178:1-321178:78", "321218:49-321218:962", "321219:1-321219:934", "321221:1-321221:40", "321230:41-321230:124", 
        "321231:1-321231:59", "321232:1-321232:30", "321233:1-321233:727", "321261:44-321261:60", "321262:1-321262:4", 
        "321283:48-321283:357", "321294:1-321294:62", "321295:1-321295:754", "321296:1-321296:67", "321305:20-321305:2659", 
        "321310:1-321310:176", "321311:1-321311:10", "321312:1-321312:768", "321313:1-321313:408", "321393:1-321393:148", 
        "321396:1-321396:1475", "321397:1-321397:365", "321414:31-321414:1283", "321415:1-321415:804", "321431:30-321431:189", 
        "321432:1-321432:47", "321433:1-321433:125", "321434:1-321434:642", "321436:1-321436:710", "321457:43-321457:451", 
        "321457:453-321457:1888", "321461:1-321461:149", "321475:50-321475:2084", "321709:44-321709:46", "321710:1-321710:57", 
        "321712:1-321712:263", "321730:2-321730:291", "321731:1-321731:9", "321732:1-321732:1448", "321735:1-321735:146", 
        "321755:33-321755:729", "321758:1-321758:189", "321759:1-321759:10", "321760:1-321760:855", "321773:11-321773:86", 
        "321774:1-321774:135", "321775:1-321775:47", "321776:1-321776:45", "321777:1-321777:279", "321778:1-321778:150", 
        "321780:1-321780:544", "321781:1-321781:676", "321794:32-321794:215", "321795:1-321795:9", "321796:1", 
        "321813:20-321813:433", "321815:1-321815:23", "321816:1-321816:5", "321817:1-321817:536", "321818:1-321818:690", 
        "321819:1-321819:8", "321820:1-321820:214", "321831:25-321831:781", "321832:1-321832:510", "321833:1-321833:407", 
        "321834:1-321834:333", "321879:39-321879:356", "321880:1-321880:41", "321880:44-321880:132", "321887:54-321887:948", 
        "321908:43-321908:472", "321909:1-321909:208", "321909:210-321909:1654", "321917:4-321917:808", "321919:1-321919:6", 
        "321933:43-321933:232", "321933:235-321933:326", "321960:18-321960:47", "321961:1-321961:354", "321973:37-321973:1253", 
        "321975:1-321975:866", "321988:45-321988:1486", "321990:1-321990:471", "322013:14-322013:22", "322014:1-322014:17", 
        "322022:42-322022:1805", "322040:32-322040:70", "322057:38-322057:58", "322068:51-322068:724", "322079:39-322079:459", 
        "322088:1-322088:596", "322106:48-322106:871", "322113:48-322113:159", "322118:1-322118:874", "322179:43-322179:820", 
        "322179:823-322179:1783", "322201:39-322201:266", "322204:1-322204:1143", "322222:1-322222:526", "322252:42-322252:1586", 
        "322317:48-322317:101", "322319:1-322319:163", "322322:1-322322:1205", "322324:1-322324:416", "322332:37-322332:1055", 
        "322348:40-322348:1505", "322355:36-322355:137", "322356:1-322356:779", "322381:45-322381:577", "322407:46-322407:582", 
        "322430:46-322430:794", "322431:1-322431:1166", "322480:60-322480:408", "322483:1-322483:8", "322484:1-322484:34", 
        "322485:1-322485:10", "322487:1-322487:47", "322492:1-322492:1386", "322510:37-322510:45", "322599:43-322599:294", 
        "322602:1-322602:69", "322602:72", "322603:1-322603:10", "322605:1-322605:280", "322616:1-322616:73", 
        "322617:1-322617:601", "322625:41-322625:1167", "322633:1-322633:249", "323413:32-323413:34", "323414:1-323414:46", 
        "323416:1-323416:74", "323417:1-323417:47", "323418:1-323418:60", "323419:1-323419:86", "323420:1-323420:34", 
        "323421:1-323421:39", "323422:1-323422:8", "323423:1-323423:149", "323470:38-323470:266", "323471:1-323471:238", 
        "323472:1-323472:112", "323473:1-323473:227", "323474:1-323474:355", "323475:1-323475:77", "323487:42-323487:498", 
        "323488:1-323488:793", "323492:1-323492:33", "323493:1-323493:144", "323495:1-323495:187", "323524:25-323524:562", 
        "323525:1-323525:1126", "323526:1-323526:466", "323693:38-323693:151", "323696:1-323696:257", "323701:1-323701:8", 
        "323702:1-323702:808", "323725:18-323725:346", "323726:1-323726:60", "323727:1-323727:987", "323755:27-323755:964", 
        "323775:38-323775:81", "323775:84-323775:171", "323778:1-323778:934", "323790:45-323790:948", "323794:1-323794:68", 
        "323841:46-323841:510", "323857:1-323857:357", "323940:49-323940:1567", "323954:1-323954:77", "323976:31-323976:85", 
        "323978:1-323978:73", "323980:1-323980:202", "323983:1-323983:188", "323997:1-323997:498", "324021:44-324021:819", 
        "324022:1-324022:554", "324077:54-324077:753", "324201:20-324201:834", "324201:837-324201:1385", "324202:1-324202:240", 
        "324205:1-324205:163", "324206:1-324206:149", "324207:1-324207:34", "324209:1-324209:142", "324237:33-324237:236", 
        "324245:23-324245:1681", "324293:39-324293:2342", "324313:24-324313:33", "324314:1-324314:8", "324315:1-324315:204", 
        "324318:1-324318:332", "324420:1-324420:625", "324564:20-324564:121", "324564:123-324564:795", "324570:150", 
        "324571:1-324571:515", "324729:1-324729:193", "324747:63-324747:1139", "324764:1-324764:150", "324765:1-324765:481", 
        "324769:1-324769:328", "324772:1-324772:165", "324785:77-324785:664", "324791:1-324791:1217", "324835:40-324835:369", 
        "324840:1-324840:96", "324841:1-324841:1347", "324846:1-324846:151", "324846:154-324846:517", "324878:62-324878:1800", 
        "324897:30-324897:170", "324970:1-324970:2195", "324980:39-324980:2340", "324997:20-324997:150", "324998:1-324998:368", 
        "324999:1-324999:44", "325000:1-325000:371", "325001:1-325001:595", "325022:45-325022:1594", "325057:42-325057:383", 
        "325097:40-325097:99", "325098:1-325098:8", "325099:1-325099:394", "325100:1-325100:254", "325101:1-325101:485", 
        "325110:1-325110:21", "325111:1-325111:22", "325113:1-325113:125", "325114:1-325114:8", "325117:1-325117:533", 
        "325159:48-325159:266", "325168:1-325168:21", "325169:1-325169:23", "325170:1-325170:692", "325170:694-325170:1205", 
        "325172:1-325172:485", "325175:1"
     ) ),
    skipEvents = cms.untracked.uint32(0)
)
process.ChargeSignificanceTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('ChargeSignificanceTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0)
)

process.CkfBaseTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.CkfTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('Chi2'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    updator = cms.string('KFUpdator')
)

process.CkfTrajectoryBuilderBeamHalo = cms.PSet(
    ComponentType = cms.string('CkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    estimator = cms.string('Chi2'),
    intermediateCleaning = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    propagatorAlong = cms.string('BeamHaloPropagatorAlong'),
    propagatorOpposite = cms.string('BeamHaloPropagatorOpposite'),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('ckfTrajectoryFilterBeamHaloMuon')
    ),
    updator = cms.string('KFUpdator')
)

process.ClusterShapeTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('ClusterShapeTrajectoryFilter'),
    cacheSrc = cms.InputTag("siPixelClusterShapeCache")
)

process.CommonClusterCheckPSet = cms.PSet(
    ClusterCollectionLabel = cms.InputTag("siStripClusters"),
    MaxNumberOfCosmicClusters = cms.uint32(400000),
    MaxNumberOfPixelClusters = cms.uint32(40000),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
    doClusterCheck = cms.bool(True)
)

process.CompositeTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet()
)

process.CosmicSeedCreator = cms.PSet(
    ComponentName = cms.string('CosmicSeedCreator'),
    MinOneOverPtError = cms.double(1.0),
    OriginTransverseErrorMultiplier = cms.double(1.0),
    SeedMomentumForBOFF = cms.double(5.0),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    maxseeds = cms.int32(10000),
    propagator = cms.string('PropagatorWithMaterialParabolicMf')
)

process.DefaultAlgorithms = cms.PSet(
    APVInspectMode = cms.string('BaselineFollower'),
    APVRestoreMode = cms.string('BaselineFollower'),
    ApplyBaselineCleaner = cms.bool(True),
    ApplyBaselineRejection = cms.bool(True),
    CleaningSequence = cms.uint32(1),
    CommonModeNoiseSubtractionMode = cms.string('IteratedMedian'),
    CutToAvoidSignal = cms.double(2.0),
    DeltaCMThreshold = cms.uint32(20),
    Deviation = cms.uint32(25),
    ForceNoRestore = cms.bool(False),
    Fraction = cms.double(0.2),
    Iterations = cms.int32(3),
    MeanCM = cms.int32(0),
    PedestalSubtractionFedMode = cms.bool(False),
    SiStripFedZeroSuppressionMode = cms.uint32(4),
    TruncateInSuppressor = cms.bool(True),
    Use10bitsTruncation = cms.bool(False),
    consecThreshold = cms.uint32(5),
    discontinuityThreshold = cms.int32(12),
    distortionThreshold = cms.uint32(20),
    doAPVRestore = cms.bool(True),
    filteredBaselineDerivativeSumSquare = cms.double(30),
    filteredBaselineMax = cms.double(6),
    hitStripThreshold = cms.uint32(40),
    lastGradient = cms.int32(10),
    minStripsToFit = cms.uint32(4),
    nSaturatedStrip = cms.uint32(2),
    nSigmaNoiseDerTh = cms.uint32(4),
    nSmooth = cms.uint32(9),
    restoreThreshold = cms.double(0.5),
    sizeWindow = cms.int32(1),
    slopeX = cms.int32(3),
    slopeY = cms.int32(4),
    useCMMeanMap = cms.bool(False),
    useRealMeanCM = cms.bool(False),
    widthCluster = cms.int32(64)
)

process.DefaultClusterizer = cms.PSet(
    Algorithm = cms.string('ThreeThresholdAlgorithm'),
    ChannelThreshold = cms.double(2.0),
    ClusterThreshold = cms.double(5.0),
    MaxAdjacentBad = cms.uint32(0),
    MaxSequentialBad = cms.uint32(1),
    MaxSequentialHoles = cms.uint32(0),
    QualityLabel = cms.string(''),
    RemoveApvShots = cms.bool(True),
    SeedThreshold = cms.double(3.0),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    )
)

process.GroupedCkfTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('Chi2'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(5),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.GroupedCkfTrajectoryBuilderP5 = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('Chi2MeasurementEstimatorForP5'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('ckfBaseTrajectoryFilterP5')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.GroupedCkfTrajectoryBuilderP5Bottom = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('MeasurementTrackerBottom'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('Chi2MeasurementEstimatorForP5'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('ckfBaseTrajectoryFilterP5')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.GroupedCkfTrajectoryBuilderP5Top = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string('MeasurementTrackerTop'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('Chi2MeasurementEstimatorForP5'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('ckfBaseTrajectoryFilterP5')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(
        0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
        0.058939, 0.125497
    ),
    HFdepthOneParameterB = cms.vdouble(
        -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
        0.000425, 0.000209
    ),
    HFdepthTwoParameterA = cms.vdouble(
        0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
        0.051579, 0.086593
    ),
    HFdepthTwoParameterB = cms.vdouble(
        -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
        0.000157, -3e-06
    )
)

process.MaxCCCLostHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MaxCCCLostHitsTrajectoryFilter'),
    maxCCCLostHits = cms.int32(3),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    )
)

process.MaxConsecLostHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MaxConsecLostHitsTrajectoryFilter'),
    maxConsecLostHits = cms.int32(1)
)

process.MaxHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MaxHitsTrajectoryFilter'),
    maxNumberOfHits = cms.int32(100)
)

process.MaxLostHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MaxLostHitsTrajectoryFilter'),
    maxLostHits = cms.int32(2)
)

process.MinHitsTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MinHitsTrajectoryFilter'),
    minimumNumberOfHits = cms.int32(5)
)

process.MinPtTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('MinPtTrajectoryFilter'),
    minHitsMinPt = cms.int32(3),
    minPt = cms.double(1.0),
    nSigmaMinPt = cms.double(5.0)
)

process.PixelTripletHLTGenerator = cms.PSet(
    ComponentName = cms.string('PixelTripletHLTGenerator'),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    extraHitRPhitolerance = cms.double(0.032),
    extraHitRZtolerance = cms.double(0.037),
    maxElement = cms.uint32(100000),
    phiPreFiltering = cms.double(0.3),
    useBending = cms.bool(True),
    useFixedPreFiltering = cms.bool(False),
    useMultScattering = cms.bool(True)
)

process.PixelTripletHLTGeneratorWithFilter = cms.PSet(
    ComponentName = cms.string('PixelTripletHLTGenerator'),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    extraHitRPhitolerance = cms.double(0.032),
    extraHitRZtolerance = cms.double(0.037),
    maxElement = cms.uint32(100000),
    phiPreFiltering = cms.double(0.3),
    useBending = cms.bool(True),
    useFixedPreFiltering = cms.bool(False),
    useMultScattering = cms.bool(True)
)

process.RegionPSetBlock = cms.PSet(
    RegionPSet = cms.PSet(
        originHalfLength = cms.double(21.2),
        originRadius = cms.double(0.2),
        originXPos = cms.double(0.0),
        originYPos = cms.double(0.0),
        originZPos = cms.double(0.0),
        precise = cms.bool(True),
        ptMin = cms.double(0.9),
        useMultipleScattering = cms.bool(False)
    )
)

process.SiStripClusterChargeCutLoose = cms.PSet(
    value = cms.double(1620.0)
)

process.SiStripClusterChargeCutNone = cms.PSet(
    value = cms.double(-1.0)
)

process.SiStripClusterChargeCutTight = cms.PSet(
    value = cms.double(1945.0)
)

process.SiStripClusterChargeCutTiny = cms.PSet(
    value = cms.double(800.0)
)

process.ThresholdPtTrajectoryFilter_block = cms.PSet(
    ComponentType = cms.string('ThresholdPtTrajectoryFilter'),
    minHitsThresholdPt = cms.int32(3),
    nSigmaThresholdPt = cms.double(5.0),
    thresholdPt = cms.double(10.0)
)

process.ckfBaseInOutTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.ckfBaseTrajectoryFilterP5 = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(3),
    maxLostHits = cms.int32(4),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.5),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.ckfTrajectoryFilterBeamHaloMuon = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(2),
    maxLostHits = cms.int32(3),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.conv2CkfTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    clustersToSkip = cms.InputTag("conv2Clusters"),
    estimator = cms.string('Chi2'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    minNrOfHitsForRebuild = cms.int32(3),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('conv2CkfTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.conv2CkfTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.convCkfTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('convStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(1),
    minNrOfHitsForRebuild = cms.int32(3),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('convCkfTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.convCkfTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(1),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.detachedQuadStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('detachedQuadStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('detachedQuadStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.detachedQuadStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('detachedQuadStepTrajectoryFilterBase')
    ))
)

process.detachedQuadStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.detachedTripletStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('detachedTripletStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('detachedTripletStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.detachedTripletStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('detachedTripletStepTrajectoryFilterBase')
    ))
)

process.detachedTripletStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.detachedTripletStepTrajectoryFilterShape = cms.PSet(
    ComponentType = cms.string('StripSubClusterShapeTrajectoryFilter'),
    layerMask = cms.PSet(
        TEC = cms.bool(False),
        TIB = cms.vuint32(1, 2),
        TID = cms.vuint32(1, 2),
        TOB = cms.bool(False)
    ),
    maxNSat = cms.uint32(3),
    maxTrimmedSizeDiffNeg = cms.double(1.0),
    maxTrimmedSizeDiffPos = cms.double(0.7),
    seedCutMIPs = cms.double(0.35),
    seedCutSN = cms.double(7.0),
    subclusterCutMIPs = cms.double(0.45),
    subclusterCutSN = cms.double(12.0),
    subclusterWindow = cms.double(0.7),
    trimMaxADC = cms.double(30.0),
    trimMaxFracNeigh = cms.double(0.25),
    trimMaxFracTotal = cms.double(0.15)
)

process.highPtTripletStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('highPtTripletStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('highPtTripletStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.highPtTripletStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('highPtTripletStepTrajectoryFilterBase')
    ))
)

process.highPtTripletStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.highPtTripletStepTrajectoryFilterInOut = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.4),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.initialStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('initialStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('initialStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.initialStepTrajectoryBuilderPreSplitting = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('initialStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('initialStepTrajectoryFilterPreSplitting')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.initialStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('initialStepTrajectoryFilterBase')
    ))
)

process.initialStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.initialStepTrajectoryFilterBasePreSplitting = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.initialStepTrajectoryFilterInOut = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.2),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(True),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(True)
)

process.initialStepTrajectoryFilterPreSplitting = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(
        cms.PSet(
            refToPSet_ = cms.string('initialStepTrajectoryFilterBasePreSplitting')
        ), 
        cms.PSet(
            refToPSet_ = cms.string('initialStepTrajectoryFilterShapePreSplitting')
        )
    )
)

process.initialStepTrajectoryFilterShape = cms.PSet(
    ComponentType = cms.string('StripSubClusterShapeTrajectoryFilter'),
    layerMask = cms.PSet(
        TEC = cms.bool(False),
        TIB = cms.vuint32(1, 2),
        TID = cms.vuint32(1, 2),
        TOB = cms.bool(False)
    ),
    maxNSat = cms.uint32(3),
    maxTrimmedSizeDiffNeg = cms.double(1.0),
    maxTrimmedSizeDiffPos = cms.double(0.7),
    seedCutMIPs = cms.double(0.35),
    seedCutSN = cms.double(7.0),
    subclusterCutMIPs = cms.double(0.45),
    subclusterCutSN = cms.double(12.0),
    subclusterWindow = cms.double(0.7),
    trimMaxADC = cms.double(30.0),
    trimMaxFracNeigh = cms.double(0.25),
    trimMaxFracTotal = cms.double(0.15)
)

process.initialStepTrajectoryFilterShapePreSplitting = cms.PSet(
    ComponentType = cms.string('StripSubClusterShapeTrajectoryFilter'),
    layerMask = cms.PSet(
        TEC = cms.bool(False),
        TIB = cms.vuint32(1, 2),
        TID = cms.vuint32(1, 2),
        TOB = cms.bool(False)
    ),
    maxNSat = cms.uint32(3),
    maxTrimmedSizeDiffNeg = cms.double(1.0),
    maxTrimmedSizeDiffPos = cms.double(0.7),
    seedCutMIPs = cms.double(0.35),
    seedCutSN = cms.double(7.0),
    subclusterCutMIPs = cms.double(0.45),
    subclusterCutSN = cms.double(12.0),
    subclusterWindow = cms.double(0.7),
    trimMaxADC = cms.double(30.0),
    trimMaxFracNeigh = cms.double(0.25),
    trimMaxFracTotal = cms.double(0.15)
)

process.jetCoreRegionalStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('jetCoreRegionalStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(50),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('jetCoreRegionalStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.jetCoreRegionalStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.layerInfo = cms.PSet(
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs')
    ),
    MTEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(5),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        useRingSlector = cms.bool(False)
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        useRingSlector = cms.bool(True)
    ),
    TID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        useRingSlector = cms.bool(False)
    )
)

process.lowPtQuadStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('lowPtQuadStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('lowPtQuadStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.lowPtQuadStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('lowPtQuadStepTrajectoryFilterBase')
    ))
)

process.lowPtQuadStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.lowPtTripletStepStandardTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.lowPtTripletStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('lowPtTripletStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(4),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('lowPtTripletStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.lowPtTripletStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('lowPtTripletStepStandardTrajectoryFilter')
    ))
)

process.lowPtTripletStepTrajectoryFilterInOut = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.075),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

process.mixedTripletStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('mixedTripletStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('mixedTripletStepPropagator'),
    propagatorOpposite = cms.string('mixedTripletStepPropagatorOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('mixedTripletStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.mixedTripletStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(1.4),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.muonSeededTrajectoryBuilderForInOut = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('muonSeededMeasurementEstimatorForInOut'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('muonSeededTrajectoryFilterForInOut')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(True),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(1.0),
    maxCand = cms.int32(5),
    minNrOfHitsForRebuild = cms.int32(2),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('muonSeededTrajectoryFilterForInOut')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.muonSeededTrajectoryBuilderForOutIn = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('muonSeededMeasurementEstimatorForOutIn'),
    foundHitBonus = cms.double(1000.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('muonSeededTrajectoryFilterForOutIn')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(1.0),
    maxCand = cms.int32(3),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('muonSeededTrajectoryFilterForOutIn')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.muonSeededTrajectoryFilterForInOut = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(10),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.muonSeededTrajectoryFilterForOutIn = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(10),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.9),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound'),
    fileMode = cms.untracked.string('NOMERGE'),
    wantSummary = cms.untracked.bool(False)
)

process.pixelLessStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('pixelLessStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('pixelLessStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.pixelLessStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.pixelPairStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(True),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('pixelPairStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('CkfBaseTrajectoryFilter_block')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(3),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(5),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('pixelPairStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(True)
)

process.pixelPairStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CompositeTrajectoryFilter'),
    filters = cms.VPSet(cms.PSet(
        refToPSet_ = cms.string('pixelPairStepTrajectoryFilterBase')
    ))
)

process.pixelPairStepTrajectoryFilterBase = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(3),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.pixelPairStepTrajectoryFilterInOut = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(0),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(999),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(1),
    seedPairPenalty = cms.int32(0),
    strictSeedExtension = cms.bool(False)
)

process.pixelPairStepTrajectoryFilterShape = cms.PSet(
    ComponentType = cms.string('StripSubClusterShapeTrajectoryFilter'),
    layerMask = cms.PSet(
        TEC = cms.bool(False),
        TIB = cms.vuint32(1, 2),
        TID = cms.vuint32(1, 2),
        TOB = cms.bool(False)
    ),
    maxNSat = cms.uint32(3),
    maxTrimmedSizeDiffNeg = cms.double(1.0),
    maxTrimmedSizeDiffPos = cms.double(0.7),
    seedCutMIPs = cms.double(0.35),
    seedCutSN = cms.double(7.0),
    subclusterCutMIPs = cms.double(0.45),
    subclusterCutSN = cms.double(12.0),
    subclusterWindow = cms.double(0.7),
    trimMaxADC = cms.double(30.0),
    trimMaxFracNeigh = cms.double(0.25),
    trimMaxFracTotal = cms.double(0.15)
)

process.tobTecStepInOutTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(4),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.tobTecStepTrajectoryBuilder = cms.PSet(
    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
    MeasurementTrackerName = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    alwaysUseInvalidHits = cms.bool(False),
    bestHitOnly = cms.bool(True),
    estimator = cms.string('tobTecStepChi2Est'),
    foundHitBonus = cms.double(10.0),
    inOutTrajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('tobTecStepInOutTrajectoryFilter')
    ),
    intermediateCleaning = cms.bool(True),
    keepOriginalIfRebuildFails = cms.bool(False),
    lockHits = cms.bool(True),
    lostHitPenalty = cms.double(30.0),
    maxCand = cms.int32(2),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7),
    minNrOfHitsForRebuild = cms.int32(4),
    propagatorAlong = cms.string('PropagatorWithMaterial'),
    propagatorOpposite = cms.string('PropagatorWithMaterialOpposite'),
    requireSeedHitsInRebuild = cms.bool(True),
    trajectoryFilter = cms.PSet(
        refToPSet_ = cms.string('tobTecStepTrajectoryFilter')
    ),
    updator = cms.string('KFUpdator'),
    useSameTrajFilter = cms.bool(False)
)

process.tobTecStepTrajectoryFilter = cms.PSet(
    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
    chargeSignificance = cms.double(-1.0),
    constantValueForLostHitsFractionFilter = cms.double(2.0),
    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
    maxCCCLostHits = cms.int32(9999),
    maxConsecLostHits = cms.int32(1),
    maxLostHits = cms.int32(0),
    maxLostHitsFraction = cms.double(0.1),
    maxNumberOfHits = cms.int32(100),
    minGoodStripCharge = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    ),
    minHitsMinPt = cms.int32(3),
    minNumberOfHitsForLoopers = cms.int32(13),
    minNumberOfHitsPerLoop = cms.int32(4),
    minPt = cms.double(0.1),
    minimumNumberOfHits = cms.int32(5),
    nSigmaMinPt = cms.double(5.0),
    pixelSeedExtension = cms.bool(False),
    seedExtension = cms.int32(0),
    seedPairPenalty = cms.int32(1),
    strictSeedExtension = cms.bool(False)
)

process.ClassifierMerger = cms.EDProducer("ClassifierMerger",
    inputClassifiers = cms.vstring()
)


process.DuplicateListMerger = cms.EDProducer("DuplicateListMerger",
    candidateComponents = cms.InputTag(""),
    candidateSource = cms.InputTag(""),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    diffHitsCut = cms.int32(5),
    mergedMVAVals = cms.InputTag(""),
    mergedSource = cms.InputTag(""),
    originalMVAVals = cms.InputTag(""),
    originalSource = cms.InputTag(""),
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder')
)


process.DuplicateTrackMerger = cms.EDProducer("DuplicateTrackMerger",
    GBRForestFileName = cms.string(''),
    chi2EstimatorName = cms.string('DuplicateTrackMergerChi2Est'),
    forestLabel = cms.string('MVADuplicate'),
    maxDCA = cms.double(30),
    maxDLambda = cms.double(0.3),
    maxDPhi = cms.double(0.3),
    maxDQoP = cms.double(0.25),
    maxDdsz = cms.double(10),
    maxDdxy = cms.double(10),
    minBDTG = cms.double(-0.1),
    minDeltaR3d = cms.double(-4),
    minP = cms.double(0.4),
    minpT = cms.double(0.2),
    overlapCheckMaxHits = cms.uint32(4),
    overlapCheckMaxMissingLayers = cms.uint32(1),
    overlapCheckMinCosT = cms.double(0.99),
    propagatorName = cms.string('PropagatorWithMaterial'),
    source = cms.InputTag(""),
    ttrhBuilderName = cms.string('WithAngleAndTemplate'),
    useInnermostState = cms.bool(True)
)


process.FinalTrackRefitter = cms.EDProducer("TrackRefitter",
    AlgorithmName = cms.string('undefAlgorithm'),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(True),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string(''),
    src = cms.InputTag("ALCARECOTkAlMinBias"),
    srcConstr = cms.InputTag(""),
    useHitsSplitting = cms.bool(False)
)


process.MeasurementTrackerEvent = cms.EDProducer("MeasurementTrackerEventProducer",
    Phase2TrackerCluster1DProducer = cms.string(''),
    badPixelFEDChannelCollectionLabels = cms.VInputTag("siPixelDigis"),
    inactivePixelDetectorLabels = cms.VInputTag("siPixelDigis"),
    inactiveStripDetectorLabels = cms.VInputTag("siStripDigis"),
    measurementTracker = cms.string(''),
    pixelCablingMapLabel = cms.string(''),
    pixelClusterProducer = cms.string('siPixelClusters'),
    skipClusters = cms.InputTag(""),
    stripClusterProducer = cms.string('siStripClusters'),
    switchOffPixelsIfEmpty = cms.bool(True)
)


process.MeasurementTrackerEventPreSplitting = cms.EDProducer("MeasurementTrackerEventProducer",
    Phase2TrackerCluster1DProducer = cms.string(''),
    badPixelFEDChannelCollectionLabels = cms.VInputTag("siPixelDigis"),
    inactivePixelDetectorLabels = cms.VInputTag("siPixelDigis"),
    inactiveStripDetectorLabels = cms.VInputTag("siStripDigis"),
    measurementTracker = cms.string(''),
    pixelCablingMapLabel = cms.string(''),
    pixelClusterProducer = cms.string('siPixelClustersPreSplitting'),
    skipClusters = cms.InputTag(""),
    stripClusterProducer = cms.string('siStripClusters'),
    switchOffPixelsIfEmpty = cms.bool(True)
)


process.MixedLayerPairs = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(1),
        minRing = cms.int32(1),
        useRingSlector = cms.bool(True)
    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg', 
        'FPix2_pos+TEC1_pos', 
        'FPix2_pos+TEC2_pos', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'FPix2_neg+TEC1_neg', 
        'FPix2_neg+TEC2_neg', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg'
    )
)


process.MixedLayerTriplets = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit")
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit")
    ),
    TID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit")
    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg', 
        'BPix1+BPix2+TIB1', 
        'BPix1+BPix3+TIB1', 
        'BPix2+BPix3+TIB1', 
        'BPix1+FPix1_pos+TID1_pos', 
        'BPix1+FPix1_neg+TID1_neg', 
        'BPix1+FPix1_pos+TID2_pos', 
        'BPix1+FPix1_neg+TID2_neg', 
        'FPix1_pos+FPix2_pos+TEC1_pos', 
        'FPix1_neg+FPix2_neg+TEC1_neg', 
        'FPix1_pos+FPix2_pos+TEC2_pos', 
        'FPix1_neg+FPix2_neg+TEC2_neg'
    )
)


process.PixelLayerPairs = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg'
    )
)


process.PixelLayerTriplets = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'
    )
)


process.TrackCollectionMerger = cms.EDProducer("TrackCollectionMerger",
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    enableMerging = cms.bool(True),
    foundHitBonus = cms.double(10),
    inputClassifiers = cms.vstring(),
    lostHitPenalty = cms.double(5),
    minQuality = cms.string('loose'),
    minShareHits = cms.uint32(2),
    shareFrac = cms.double(0.19),
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
    trackProducers = cms.VInputTag()
)


process.TrackCutClassifier = cms.EDProducer("TrackCutClassifier",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            drWPVerr_par = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dr_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dr_par1 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dr_par2 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38)
        ),
        dz_par = cms.PSet(
            dzWPVerr_par = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dz_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dz_par1 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dz_par2 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38)
        ),
        isHLT = cms.bool(False),
        maxChi2 = cms.vdouble(9999, 25, 16),
        maxChi2n = cms.vdouble(9999, 1, 0.4),
        maxDr = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        maxDz = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24, 15),
        maxLostLayers = cms.vint32(99, 3, 3),
        maxRelPtErr = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        min3DLayers = cms.vint32(1, 2, 3),
        minHits = cms.vint32(0, 0, 1),
        minHits4pass = cms.vint32(2147483647, 2147483647, 2147483647),
        minLayers = cms.vint32(3, 4, 5),
        minNVtxTrk = cms.int32(2),
        minNdof = cms.vdouble(-1, -1, -1),
        minPixelHits = cms.vint32(0, 0, 1)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag(""),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.TrackLwtnnClassifier = cms.EDProducer("TrackLwtnnClassifier",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        lwtnnLabel = cms.string('trackSelectionLwtnn')
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag(""),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.TrackMVAClassifierDetached = cms.EDProducer("TrackMVAClassifierDetached",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('')
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag(""),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.TrackMVAClassifierPrompt = cms.EDProducer("TrackMVAClassifierPrompt",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('')
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag(""),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.TrackProducer = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('undefAlgorithm'),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("ckfTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.TrackRefitter = cms.EDProducer("TrackRefitter",
    AlgorithmName = cms.string('undefAlgorithm'),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(True),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string(''),
    src = cms.InputTag("generalTracks"),
    srcConstr = cms.InputTag(""),
    useHitsSplitting = cms.bool(False)
)


process.TrackRefitterBHM = cms.EDProducer("TrackRefitter",
    AlgorithmName = cms.string('undefAlgorithm'),
    Fitter = cms.string('KFFittingSmootherBH'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('BeamHaloPropagatorAlong'),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(True),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string(''),
    src = cms.InputTag("ctfWithMaterialTracksBeamHaloMuon"),
    srcConstr = cms.InputTag(""),
    useHitsSplitting = cms.bool(False)
)


process.TrackRefitterP5 = cms.EDProducer("TrackRefitter",
    AlgorithmName = cms.string('ctf'),
    Fitter = cms.string('FittingSmootherRKP5'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(True),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string(''),
    src = cms.InputTag("ctfWithMaterialTracksP5"),
    srcConstr = cms.InputTag(""),
    useHitsSplitting = cms.bool(False)
)


process.ak4CaloJetsForTrk = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(True),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("caloTowerForTrk"),
    srcPVs = cms.InputTag("firstStepPrimaryVerticesUnsorted"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4CaloJetsForTrkPreSplitting = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(True),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.3),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('CaloJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    puPtMin = cms.double(10),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("caloTowerForTrkPreSplitting"),
    srcPVs = cms.InputTag("firstStepPrimaryVerticesPreSplitting"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.beamhaloTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('BeamHaloNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('CkfTrajectoryBuilderBeamHalo')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('BeamHaloPropagatorAlong'),
        propagatorOppositeTISE = cms.string('BeamHaloPropagatorOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("beamhaloTrackerSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.beamhaloTrackerSeedingLayers = cms.EDProducer("SeedingLayersEDProducer",
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelPairs')
    ),
    MTEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(5),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        useRingSlector = cms.bool(False)
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        useRingSlector = cms.bool(True)
    ),
    TID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        useRingSlector = cms.bool(False)
    ),
    layerList = cms.vstring(
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg', 
        'TID2_pos+TID3_pos', 
        'TID2_neg+TID3_neg', 
        'TEC1_neg+TEC2_neg', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_neg+TEC3_neg', 
        'TEC2_pos+TEC3_pos', 
        'TEC3_neg+TEC4_neg', 
        'TEC3_pos+TEC4_pos', 
        'TEC4_neg+TEC5_neg', 
        'TEC4_pos+TEC5_pos', 
        'TEC5_neg+TEC6_neg', 
        'TEC5_pos+TEC6_pos', 
        'MTEC7_neg+MTEC8_neg', 
        'MTEC7_pos+MTEC8_pos', 
        'MTEC8_neg+MTEC9_neg', 
        'MTEC8_pos+MTEC9_pos'
    )
)


process.beamhaloTrackerSeeds = cms.EDProducer("CtfSpecialSeedGenerator",
    Charges = cms.vint32(-1, 1),
    CheckHitsAreOnDifferentLayers = cms.bool(False),
    ClusterCollectionLabel = cms.InputTag("siStripClusters"),
    ErrorRescaling = cms.double(50.0),
    MaxNumberOfCosmicClusters = cms.uint32(10000),
    MaxNumberOfPixelClusters = cms.uint32(10000),
    OrderedHitsFactoryPSets = cms.VPSet(
        cms.PSet(
            ComponentName = cms.string('BeamHaloPairGenerator'),
            LayerSrc = cms.InputTag("beamhaloTrackerSeedingLayers"),
            NavigationDirection = cms.string('outsideIn'),
            PropagationDirection = cms.string('alongMomentum'),
            maxTheta = cms.double(0.1)
        ), 
        cms.PSet(
            ComponentName = cms.string('BeamHaloPairGenerator'),
            LayerSrc = cms.InputTag("beamhaloTrackerSeedingLayers"),
            NavigationDirection = cms.string('outsideIn'),
            PropagationDirection = cms.string('oppositeToMomentum'),
            maxTheta = cms.double(0.1)
        )
    ),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducer'),
        RegionPSet = cms.PSet(
            originHalfLength = cms.double(21.2),
            originRadius = cms.double(0.2),
            originXPos = cms.double(0.0),
            originYPos = cms.double(0.0),
            originZPos = cms.double(0.0),
            precise = cms.bool(True),
            ptMin = cms.double(0.9),
            useMultipleScattering = cms.bool(False)
        )
    ),
    SeedMomentum = cms.double(15.0),
    SeedsFromNegativeY = cms.bool(False),
    SeedsFromPositiveY = cms.bool(False),
    SetMomentum = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    UseScintillatorsConstraint = cms.bool(False),
    doClusterCheck = cms.bool(True),
    maxSeeds = cms.int32(10000),
    requireBOFF = cms.bool(False)
)


process.beamhaloTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('beamhalo'),
    Fitter = cms.string('KFFittingSmootherBH'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('BeamHaloNavigationSchool'),
    Propagator = cms.string('BeamHaloPropagatorAlong'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('beamhaloTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("beamhaloTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.caloTowerForTrk = cms.EDProducer("CaloTowersCreator",
    AllowMissingInputs = cms.bool(False),
    EBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    EBSumThreshold = cms.double(0.2),
    EBThreshold = cms.double(0.07),
    EBWeight = cms.double(1.0),
    EBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    EEGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    EESumThreshold = cms.double(0.45),
    EEThreshold = cms.double(0.3),
    EEWeight = cms.double(1.0),
    EEWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring(
        'kTime', 
        'kWeird', 
        'kBad'
    ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(),
    EcutTower = cms.double(-1000.0),
    HBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HBThreshold = cms.double(0.7),
    HBThreshold1 = cms.double(0.7),
    HBThreshold2 = cms.double(0.7),
    HBWeight = cms.double(1.0),
    HBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HEDGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HEDThreshold = cms.double(0.8),
    HEDThreshold1 = cms.double(0.8),
    HEDWeight = cms.double(1.0),
    HEDWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HESGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HESThreshold = cms.double(0.8),
    HESThreshold1 = cms.double(0.8),
    HESWeight = cms.double(1.0),
    HESWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HF1Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HF1Threshold = cms.double(0.5),
    HF1Weight = cms.double(1.0),
    HF1Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HF2Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HF2Threshold = cms.double(0.85),
    HF2Weight = cms.double(1.0),
    HF2Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HOGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HOThreshold0 = cms.double(1.1),
    HOThresholdMinus1 = cms.double(3.5),
    HOThresholdMinus2 = cms.double(3.5),
    HOThresholdPlus1 = cms.double(3.5),
    HOThresholdPlus2 = cms.double(3.5),
    HOWeight = cms.double(1.0),
    HOWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HcalAcceptSeverityLevel = cms.uint32(9),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32(9999),
    HcalPhase = cms.int32(0),
    HcalThreshold = cms.double(-1000.0),
    MomConstrMethod = cms.int32(1),
    MomEBDepth = cms.double(0.3),
    MomEEDepth = cms.double(0.0),
    MomHBDepth = cms.double(0.2),
    MomHEDepth = cms.double(0.4),
    UseEcalRecoveredHits = cms.bool(False),
    UseEtEBTreshold = cms.bool(False),
    UseEtEETreshold = cms.bool(False),
    UseHO = cms.bool(True),
    UseHcalRecoveredHits = cms.bool(True),
    UseRejectedHitsOnly = cms.bool(False),
    UseRejectedRecoveredEcalHits = cms.bool(False),
    UseRejectedRecoveredHcalHits = cms.bool(True),
    UseSymEBTreshold = cms.bool(True),
    UseSymEETreshold = cms.bool(True),
    ecalInputs = cms.VInputTag(cms.InputTag("ecalRecHit","EcalRecHitsEB"), cms.InputTag("ecalRecHit","EcalRecHitsEE")),
    hbheInput = cms.InputTag("hbheprereco"),
    hfInput = cms.InputTag("hfreco"),
    hoInput = cms.InputTag("horeco"),
    missingHcalRescaleFactorForEcal = cms.double(0)
)


process.caloTowerForTrkPreSplitting = cms.EDProducer("CaloTowersCreator",
    AllowMissingInputs = cms.bool(False),
    EBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    EBSumThreshold = cms.double(0.2),
    EBThreshold = cms.double(0.07),
    EBWeight = cms.double(1.0),
    EBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    EEGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    EESumThreshold = cms.double(0.45),
    EEThreshold = cms.double(0.3),
    EEWeight = cms.double(1.0),
    EEWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring(
        'kTime', 
        'kWeird', 
        'kBad'
    ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(),
    EcutTower = cms.double(-1000.0),
    HBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HBThreshold = cms.double(0.7),
    HBThreshold1 = cms.double(0.7),
    HBThreshold2 = cms.double(0.7),
    HBWeight = cms.double(1.0),
    HBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HEDGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HEDThreshold = cms.double(0.8),
    HEDThreshold1 = cms.double(0.8),
    HEDWeight = cms.double(1.0),
    HEDWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HESGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HESThreshold = cms.double(0.8),
    HESThreshold1 = cms.double(0.8),
    HESWeight = cms.double(1.0),
    HESWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HF1Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HF1Threshold = cms.double(0.5),
    HF1Weight = cms.double(1.0),
    HF1Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HF2Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HF2Threshold = cms.double(0.85),
    HF2Weight = cms.double(1.0),
    HF2Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HOGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HOThreshold0 = cms.double(1.1),
    HOThresholdMinus1 = cms.double(3.5),
    HOThresholdMinus2 = cms.double(3.5),
    HOThresholdPlus1 = cms.double(3.5),
    HOThresholdPlus2 = cms.double(3.5),
    HOWeight = cms.double(1.0),
    HOWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HcalAcceptSeverityLevel = cms.uint32(9),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32(9999),
    HcalPhase = cms.int32(0),
    HcalThreshold = cms.double(-1000.0),
    MomConstrMethod = cms.int32(1),
    MomEBDepth = cms.double(0.3),
    MomEEDepth = cms.double(0.0),
    MomHBDepth = cms.double(0.2),
    MomHEDepth = cms.double(0.4),
    UseEcalRecoveredHits = cms.bool(False),
    UseEtEBTreshold = cms.bool(False),
    UseEtEETreshold = cms.bool(False),
    UseHO = cms.bool(True),
    UseHcalRecoveredHits = cms.bool(True),
    UseRejectedHitsOnly = cms.bool(False),
    UseRejectedRecoveredEcalHits = cms.bool(False),
    UseRejectedRecoveredHcalHits = cms.bool(True),
    UseSymEBTreshold = cms.bool(True),
    UseSymEETreshold = cms.bool(True),
    ecalInputs = cms.VInputTag(cms.InputTag("ecalRecHit","EcalRecHitsEB"), cms.InputTag("ecalRecHit","EcalRecHitsEE")),
    hbheInput = cms.InputTag("hbheprereco"),
    hfInput = cms.InputTag("hfreco"),
    hoInput = cms.InputTag("horeco"),
    missingHcalRescaleFactorForEcal = cms.double(0)
)


process.calotowermaker = cms.EDProducer("CaloTowersCreator",
    AllowMissingInputs = cms.bool(False),
    EBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    EBSumThreshold = cms.double(0.2),
    EBThreshold = cms.double(0.07),
    EBWeight = cms.double(1.0),
    EBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    EEGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    EESumThreshold = cms.double(0.45),
    EEThreshold = cms.double(0.3),
    EEWeight = cms.double(1.0),
    EEWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring(
        'kTime', 
        'kWeird', 
        'kBad'
    ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(),
    EcutTower = cms.double(-1000.0),
    HBGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HBThreshold = cms.double(0.7),
    HBThreshold1 = cms.double(0.7),
    HBThreshold2 = cms.double(0.7),
    HBWeight = cms.double(1.0),
    HBWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HEDGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HEDThreshold = cms.double(0.8),
    HEDThreshold1 = cms.double(0.8),
    HEDWeight = cms.double(1.0),
    HEDWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HESGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HESThreshold = cms.double(0.8),
    HESThreshold1 = cms.double(0.8),
    HESWeight = cms.double(1.0),
    HESWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HF1Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HF1Threshold = cms.double(0.5),
    HF1Weight = cms.double(1.0),
    HF1Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HF2Grid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HF2Threshold = cms.double(0.85),
    HF2Weight = cms.double(1.0),
    HF2Weights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HOGrid = cms.vdouble(-1.0, 1.0, 10.0, 100.0, 1000.0),
    HOThreshold0 = cms.double(1.1),
    HOThresholdMinus1 = cms.double(3.5),
    HOThresholdMinus2 = cms.double(3.5),
    HOThresholdPlus1 = cms.double(3.5),
    HOThresholdPlus2 = cms.double(3.5),
    HOWeight = cms.double(1.0),
    HOWeights = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0),
    HcalAcceptSeverityLevel = cms.uint32(9),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32(9999),
    HcalPhase = cms.int32(0),
    HcalThreshold = cms.double(-1000.0),
    MomConstrMethod = cms.int32(1),
    MomEBDepth = cms.double(0.3),
    MomEEDepth = cms.double(0.0),
    MomHBDepth = cms.double(0.2),
    MomHEDepth = cms.double(0.4),
    UseEcalRecoveredHits = cms.bool(False),
    UseEtEBTreshold = cms.bool(False),
    UseEtEETreshold = cms.bool(False),
    UseHO = cms.bool(True),
    UseHcalRecoveredHits = cms.bool(True),
    UseRejectedHitsOnly = cms.bool(False),
    UseRejectedRecoveredEcalHits = cms.bool(False),
    UseRejectedRecoveredHcalHits = cms.bool(True),
    UseSymEBTreshold = cms.bool(True),
    UseSymEETreshold = cms.bool(True),
    ecalInputs = cms.VInputTag(cms.InputTag("ecalRecHit","EcalRecHitsEB"), cms.InputTag("ecalRecHit","EcalRecHitsEE")),
    hbheInput = cms.InputTag("hbhereco"),
    hfInput = cms.InputTag("hfreco"),
    hoInput = cms.InputTag("horeco"),
    missingHcalRescaleFactorForEcal = cms.double(0)
)


process.chargeCut2069Clusters = cms.EDProducer("ClusterChargeMasker",
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    ),
    oldClusterRemovalInfo = cms.InputTag("pixelPairStepClusters"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters")
)


process.ckfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('GroupedCkfTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("globalMixedSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.ckfTrackCandidatesCombinedSeeds = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('GroupedCkfTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("globalCombinedSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.ckfTrackCandidatesNoOverlaps = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('CkfTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("globalMixedSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.ckfTrackCandidatesP5 = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('CosmicNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('GroupedCkfTrajectoryBuilderP5')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("combinedP5SeedsForCTF"),
    useHitsSplitting = cms.bool(True)
)


process.ckfTrackCandidatesP5Bottom = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('CosmicNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('GroupedCkfTrajectoryBuilderP5Bottom')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("combinedP5SeedsForCTFBottom"),
    useHitsSplitting = cms.bool(True)
)


process.ckfTrackCandidatesP5LHCNavigation = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('GroupedCkfTrajectoryBuilderP5')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("combinedP5SeedsForCTF"),
    useHitsSplitting = cms.bool(True)
)


process.ckfTrackCandidatesP5Top = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('CosmicNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('GroupedCkfTrajectoryBuilderP5Top')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("combinedP5SeedsForCTFTop"),
    useHitsSplitting = cms.bool(True)
)


process.ckfTrackCandidatesPixelLess = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('GroupedCkfTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("globalPixelLessSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.combinatorialcosmicseedfinder = cms.EDProducer("CtfSpecialSeedGenerator",
    Charges = cms.vint32(-1),
    CheckHitsAreOnDifferentLayers = cms.bool(False),
    ClusterCollectionLabel = cms.InputTag("siStripClusters"),
    DontCountDetsAboveNClusters = cms.uint32(20),
    ErrorRescaling = cms.double(50.0),
    LowerScintillatorParameters = cms.PSet(
        GlobalX = cms.double(0.0),
        GlobalY = cms.double(-100.0),
        GlobalZ = cms.double(50.0),
        LenghtInZ = cms.double(100.0),
        WidthInX = cms.double(100.0)
    ),
    MaxNumberOfCosmicClusters = cms.uint32(300),
    MaxNumberOfPixelClusters = cms.uint32(300),
    OrderedHitsFactoryPSets = cms.VPSet(
        cms.PSet(
            ComponentName = cms.string('GenericTripletGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingtripletsTOB"),
            NavigationDirection = cms.string('outsideIn'),
            PropagationDirection = cms.string('alongMomentum')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingpairsTECpos"),
            NavigationDirection = cms.string('outsideIn'),
            PropagationDirection = cms.string('alongMomentum')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericTripletGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingtripletsTIB"),
            NavigationDirection = cms.string('insideOut'),
            PropagationDirection = cms.string('oppositeToMomentum')
        )
    ),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducer'),
        RegionPSet = cms.PSet(
            originHalfLength = cms.double(21.2),
            originRadius = cms.double(0.2),
            originXPos = cms.double(0.0),
            originYPos = cms.double(0.0),
            originZPos = cms.double(0.0),
            precise = cms.bool(True),
            ptMin = cms.double(0.9),
            useMultipleScattering = cms.bool(False)
        )
    ),
    SeedMomentum = cms.double(5.0),
    SeedsFromNegativeY = cms.bool(False),
    SeedsFromPositiveY = cms.bool(True),
    SetMomentum = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    UpperScintillatorParameters = cms.PSet(
        GlobalX = cms.double(0.0),
        GlobalY = cms.double(300.0),
        GlobalZ = cms.double(50.0),
        LenghtInZ = cms.double(100.0),
        WidthInX = cms.double(100.0)
    ),
    UseScintillatorsConstraint = cms.bool(True),
    doClusterCheck = cms.bool(True),
    maxSeeds = cms.int32(10000),
    requireBOFF = cms.bool(False)
)


process.combinatorialcosmicseedfinderP5 = cms.EDProducer("CtfSpecialSeedGenerator",
    Charges = cms.vint32(-1),
    CheckHitsAreOnDifferentLayers = cms.bool(False),
    ClusterCollectionLabel = cms.InputTag("siStripClusters"),
    DontCountDetsAboveNClusters = cms.uint32(20),
    ErrorRescaling = cms.double(50.0),
    LowerScintillatorParameters = cms.PSet(
        GlobalX = cms.double(0.0),
        GlobalY = cms.double(-100.0),
        GlobalZ = cms.double(50.0),
        LenghtInZ = cms.double(100.0),
        WidthInX = cms.double(100.0)
    ),
    MaxNumberOfCosmicClusters = cms.uint32(300),
    MaxNumberOfPixelClusters = cms.uint32(300),
    OrderedHitsFactoryPSets = cms.VPSet(
        cms.PSet(
            ComponentName = cms.string('GenericTripletGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingtripletsP5"),
            NavigationDirection = cms.string('outsideIn'),
            PropagationDirection = cms.string('alongMomentum')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingpairsTOBP5"),
            NavigationDirection = cms.string('outsideIn'),
            PropagationDirection = cms.string('alongMomentum')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingpairsTECposP5"),
            NavigationDirection = cms.string('outsideIn'),
            PropagationDirection = cms.string('alongMomentum')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingpairsTECposP5"),
            NavigationDirection = cms.string('insideOut'),
            PropagationDirection = cms.string('alongMomentum')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingpairsTECnegP5"),
            NavigationDirection = cms.string('outsideIn'),
            PropagationDirection = cms.string('alongMomentum')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingpairsTECnegP5"),
            NavigationDirection = cms.string('insideOut'),
            PropagationDirection = cms.string('alongMomentum')
        )
    ),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducer'),
        RegionPSet = cms.PSet(
            originHalfLength = cms.double(21.2),
            originRadius = cms.double(0.2),
            originXPos = cms.double(0.0),
            originYPos = cms.double(0.0),
            originZPos = cms.double(0.0),
            precise = cms.bool(True),
            ptMin = cms.double(0.9),
            useMultipleScattering = cms.bool(False)
        )
    ),
    SeedMomentum = cms.double(5.0),
    SeedsFromNegativeY = cms.bool(False),
    SeedsFromPositiveY = cms.bool(True),
    SetMomentum = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    UpperScintillatorParameters = cms.PSet(
        GlobalX = cms.double(0.0),
        GlobalY = cms.double(300.0),
        GlobalZ = cms.double(50.0),
        LenghtInZ = cms.double(100.0),
        WidthInX = cms.double(100.0)
    ),
    UseScintillatorsConstraint = cms.bool(False),
    doClusterCheck = cms.bool(True),
    maxSeeds = cms.int32(10000),
    requireBOFF = cms.bool(True)
)


process.combinatorialcosmicseedfinderP5Bottom = cms.EDProducer("CtfSpecialSeedGenerator",
    Charges = cms.vint32(-1),
    CheckHitsAreOnDifferentLayers = cms.bool(False),
    ClusterCollectionLabel = cms.InputTag("siStripClustersBottom"),
    DontCountDetsAboveNClusters = cms.uint32(20),
    ErrorRescaling = cms.double(50.0),
    LowerScintillatorParameters = cms.PSet(
        GlobalX = cms.double(0.0),
        GlobalY = cms.double(-100.0),
        GlobalZ = cms.double(50.0),
        LenghtInZ = cms.double(100.0),
        WidthInX = cms.double(100.0)
    ),
    MaxNumberOfCosmicClusters = cms.uint32(150),
    MaxNumberOfPixelClusters = cms.uint32(300),
    OrderedHitsFactoryPSets = cms.VPSet(
        cms.PSet(
            ComponentName = cms.string('GenericTripletGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingtripletsP5Bottom"),
            NavigationDirection = cms.string('outsideIn'),
            PropagationDirection = cms.string('oppositeToMomentum')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingpairsTOBP5Bottom"),
            NavigationDirection = cms.string('outsideIn'),
            PropagationDirection = cms.string('oppositeToMomentum')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingpairsTECposP5Bottom"),
            NavigationDirection = cms.string('outsideIn'),
            PropagationDirection = cms.string('oppositeToMomentum')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingpairsTECposP5Bottom"),
            NavigationDirection = cms.string('insideOut'),
            PropagationDirection = cms.string('oppositeToMomentum')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingpairsTECnegP5Bottom"),
            NavigationDirection = cms.string('outsideIn'),
            PropagationDirection = cms.string('oppositeToMomentum')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingpairsTECnegP5Bottom"),
            NavigationDirection = cms.string('insideOut'),
            PropagationDirection = cms.string('oppositeToMomentum')
        )
    ),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducer'),
        RegionPSet = cms.PSet(
            originHalfLength = cms.double(21.2),
            originRadius = cms.double(0.2),
            originXPos = cms.double(0.0),
            originYPos = cms.double(0.0),
            originZPos = cms.double(0.0),
            precise = cms.bool(True),
            ptMin = cms.double(0.9),
            useMultipleScattering = cms.bool(False)
        )
    ),
    SeedMomentum = cms.double(5.0),
    SeedsFromNegativeY = cms.bool(True),
    SeedsFromPositiveY = cms.bool(False),
    SetMomentum = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    UpperScintillatorParameters = cms.PSet(
        GlobalX = cms.double(0.0),
        GlobalY = cms.double(300.0),
        GlobalZ = cms.double(50.0),
        LenghtInZ = cms.double(100.0),
        WidthInX = cms.double(100.0)
    ),
    UseScintillatorsConstraint = cms.bool(False),
    doClusterCheck = cms.bool(True),
    maxSeeds = cms.int32(10000),
    requireBOFF = cms.bool(True)
)


process.combinatorialcosmicseedfinderP5Top = cms.EDProducer("CtfSpecialSeedGenerator",
    Charges = cms.vint32(-1),
    CheckHitsAreOnDifferentLayers = cms.bool(False),
    ClusterCollectionLabel = cms.InputTag("siStripClustersTop"),
    DontCountDetsAboveNClusters = cms.uint32(20),
    ErrorRescaling = cms.double(50.0),
    LowerScintillatorParameters = cms.PSet(
        GlobalX = cms.double(0.0),
        GlobalY = cms.double(-100.0),
        GlobalZ = cms.double(50.0),
        LenghtInZ = cms.double(100.0),
        WidthInX = cms.double(100.0)
    ),
    MaxNumberOfCosmicClusters = cms.uint32(150),
    MaxNumberOfPixelClusters = cms.uint32(300),
    OrderedHitsFactoryPSets = cms.VPSet(
        cms.PSet(
            ComponentName = cms.string('GenericTripletGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingtripletsP5Top"),
            NavigationDirection = cms.string('outsideIn'),
            PropagationDirection = cms.string('alongMomentum')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingpairsTOBP5Top"),
            NavigationDirection = cms.string('outsideIn'),
            PropagationDirection = cms.string('alongMomentum')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingpairsTECposP5Top"),
            NavigationDirection = cms.string('outsideIn'),
            PropagationDirection = cms.string('alongMomentum')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingpairsTECposP5Top"),
            NavigationDirection = cms.string('insideOut'),
            PropagationDirection = cms.string('alongMomentum')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingpairsTECnegP5Top"),
            NavigationDirection = cms.string('outsideIn'),
            PropagationDirection = cms.string('alongMomentum')
        ), 
        cms.PSet(
            ComponentName = cms.string('GenericPairGenerator'),
            LayerSrc = cms.InputTag("combinatorialcosmicseedingpairsTECnegP5Top"),
            NavigationDirection = cms.string('insideOut'),
            PropagationDirection = cms.string('alongMomentum')
        )
    ),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducer'),
        RegionPSet = cms.PSet(
            originHalfLength = cms.double(21.2),
            originRadius = cms.double(0.2),
            originXPos = cms.double(0.0),
            originYPos = cms.double(0.0),
            originZPos = cms.double(0.0),
            precise = cms.bool(True),
            ptMin = cms.double(0.9),
            useMultipleScattering = cms.bool(False)
        )
    ),
    SeedMomentum = cms.double(5.0),
    SeedsFromNegativeY = cms.bool(False),
    SeedsFromPositiveY = cms.bool(True),
    SetMomentum = cms.bool(True),
    TTRHBuilder = cms.string('WithTrackAngle'),
    UpperScintillatorParameters = cms.PSet(
        GlobalX = cms.double(0.0),
        GlobalY = cms.double(300.0),
        GlobalZ = cms.double(50.0),
        LenghtInZ = cms.double(100.0),
        WidthInX = cms.double(100.0)
    ),
    UseScintillatorsConstraint = cms.bool(False),
    doClusterCheck = cms.bool(True),
    maxSeeds = cms.int32(10000),
    requireBOFF = cms.bool(True)
)


process.combinatorialcosmicseedingpairsTECnegP5 = cms.EDProducer("SeedingLayersEDProducer",
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(5),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        useRingSlector = cms.bool(True)
    ),
    layerList = cms.vstring(
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg', 
        'TEC3_neg+TEC4_neg', 
        'TEC4_neg+TEC5_neg', 
        'TEC5_neg+TEC6_neg', 
        'TEC6_neg+TEC7_neg', 
        'TEC7_neg+TEC8_neg', 
        'TEC8_neg+TEC9_neg'
    )
)


process.combinatorialcosmicseedingpairsTECnegP5Bottom = cms.EDProducer("SeedingLayersEDProducer",
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(5),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
        useRingSlector = cms.bool(True)
    ),
    layerList = cms.vstring(
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg', 
        'TEC3_neg+TEC4_neg', 
        'TEC4_neg+TEC5_neg', 
        'TEC5_neg+TEC6_neg', 
        'TEC6_neg+TEC7_neg', 
        'TEC7_neg+TEC8_neg', 
        'TEC8_neg+TEC9_neg'
    )
)


process.combinatorialcosmicseedingpairsTECnegP5Top = cms.EDProducer("SeedingLayersEDProducer",
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(5),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
        useRingSlector = cms.bool(True)
    ),
    layerList = cms.vstring(
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg', 
        'TEC3_neg+TEC4_neg', 
        'TEC4_neg+TEC5_neg', 
        'TEC5_neg+TEC6_neg', 
        'TEC6_neg+TEC7_neg', 
        'TEC7_neg+TEC8_neg', 
        'TEC8_neg+TEC9_neg'
    )
)


process.combinatorialcosmicseedingpairsTECposP5 = cms.EDProducer("SeedingLayersEDProducer",
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(5),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        useRingSlector = cms.bool(True)
    ),
    layerList = cms.vstring(
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TEC3_pos+TEC4_pos', 
        'TEC4_pos+TEC5_pos', 
        'TEC5_pos+TEC6_pos', 
        'TEC6_pos+TEC7_pos', 
        'TEC7_pos+TEC8_pos', 
        'TEC8_pos+TEC9_pos'
    )
)


process.combinatorialcosmicseedingpairsTECposP5Bottom = cms.EDProducer("SeedingLayersEDProducer",
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(5),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
        useRingSlector = cms.bool(True)
    ),
    layerList = cms.vstring(
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TEC3_pos+TEC4_pos', 
        'TEC4_pos+TEC5_pos', 
        'TEC5_pos+TEC6_pos', 
        'TEC6_pos+TEC7_pos', 
        'TEC7_pos+TEC8_pos', 
        'TEC8_pos+TEC9_pos'
    )
)


process.combinatorialcosmicseedingpairsTECposP5Top = cms.EDProducer("SeedingLayersEDProducer",
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(5),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
        useRingSlector = cms.bool(True)
    ),
    layerList = cms.vstring(
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TEC3_pos+TEC4_pos', 
        'TEC4_pos+TEC5_pos', 
        'TEC5_pos+TEC6_pos', 
        'TEC6_pos+TEC7_pos', 
        'TEC7_pos+TEC8_pos', 
        'TEC8_pos+TEC9_pos'
    )
)


process.combinatorialcosmicseedingpairsTOBP5 = cms.EDProducer("SeedingLayersEDProducer",
    MTIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    ),
    MTOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(5),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        useRingSlector = cms.bool(False),
        useSimpleRphiHitsCleaner = cms.bool(True)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit")
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit")
    ),
    layerList = cms.vstring(
        'MTOB5+MTOB6', 
        'MTOB4+MTOB5'
    )
)


process.combinatorialcosmicseedingpairsTOBP5Bottom = cms.EDProducer("SeedingLayersEDProducer",
    MTIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
    ),
    MTOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(5),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
        useRingSlector = cms.bool(False),
        useSimpleRphiHitsCleaner = cms.bool(True)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit")
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit")
    ),
    layerList = cms.vstring(
        'MTOB5+MTOB6', 
        'MTOB4+MTOB5'
    )
)


process.combinatorialcosmicseedingpairsTOBP5Top = cms.EDProducer("SeedingLayersEDProducer",
    MTIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
    ),
    MTOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(5),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
        useRingSlector = cms.bool(False),
        useSimpleRphiHitsCleaner = cms.bool(True)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit")
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit")
    ),
    layerList = cms.vstring(
        'MTOB5+MTOB6', 
        'MTOB4+MTOB5'
    )
)


process.combinatorialcosmicseedingtripletsP5 = cms.EDProducer("SeedingLayersEDProducer",
    MTIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    ),
    MTOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(5),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        useRingSlector = cms.bool(False),
        useSimpleRphiHitsCleaner = cms.bool(True)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit")
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit")
    ),
    layerList = cms.vstring(
        'MTOB4+MTOB5+MTOB6', 
        'MTOB3+MTOB5+MTOB6', 
        'MTOB3+MTOB4+MTOB5', 
        'TOB2+MTOB4+MTOB5', 
        'MTOB3+MTOB4+MTOB6', 
        'TOB2+MTOB4+MTOB6'
    )
)


process.combinatorialcosmicseedingtripletsP5Bottom = cms.EDProducer("SeedingLayersEDProducer",
    MTIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
    ),
    MTOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(5),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
        useRingSlector = cms.bool(False),
        useSimpleRphiHitsCleaner = cms.bool(True)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit")
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit")
    ),
    layerList = cms.vstring(
        'MTOB4+MTOB5+MTOB6', 
        'MTOB3+MTOB5+MTOB6', 
        'MTOB3+MTOB4+MTOB5', 
        'TOB2+MTOB4+MTOB5', 
        'MTOB3+MTOB4+MTOB6', 
        'TOB2+MTOB4+MTOB6'
    )
)


process.combinatorialcosmicseedingtripletsP5Top = cms.EDProducer("SeedingLayersEDProducer",
    MTIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
    ),
    MTOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(5),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
        useRingSlector = cms.bool(False),
        useSimpleRphiHitsCleaner = cms.bool(True)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit")
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit")
    ),
    layerList = cms.vstring(
        'MTOB4+MTOB5+MTOB6', 
        'MTOB3+MTOB5+MTOB6', 
        'MTOB3+MTOB4+MTOB5', 
        'TOB2+MTOB4+MTOB5', 
        'MTOB3+MTOB4+MTOB6', 
        'TOB2+MTOB4+MTOB6'
    )
)


process.combinedP5SeedsForCTF = cms.EDProducer("SeedCombiner",
    PairCollection = cms.InputTag("combinatorialcosmicseedfinderP5"),
    TripletCollection = cms.InputTag("simpleCosmicBONSeeds"),
    seedCollections = cms.VInputTag(cms.InputTag("combinatorialcosmicseedfinderP5"), cms.InputTag("simpleCosmicBONSeeds"))
)


process.combinedP5SeedsForCTFBottom = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag(cms.InputTag("combinatorialcosmicseedfinderP5Bottom"), cms.InputTag("simpleCosmicBONSeedsBottom"))
)


process.combinedP5SeedsForCTFTop = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag(cms.InputTag("combinatorialcosmicseedfinderP5Top"), cms.InputTag("simpleCosmicBONSeedsTop"))
)


process.conv2Clusters = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(30.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag("convClusters"),
    overrideTrkQuals = cms.InputTag("convStepSelector","convStep"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trackClassifier = cms.InputTag("","QualityMasks"),
    trajectories = cms.InputTag("convStepTracks")
)


process.conv2LayerPairs = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("conv2Clusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("conv2Clusters")
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(1),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        skipClusters = cms.InputTag("conv2Clusters"),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        useRingSlector = cms.bool(True),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TIB1 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        skipClusters = cms.InputTag("conv2Clusters")
    ),
    TIB2 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        skipClusters = cms.InputTag("conv2Clusters")
    ),
    TIB3 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        skipClusters = cms.InputTag("conv2Clusters")
    ),
    TIB4 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        skipClusters = cms.InputTag("conv2Clusters")
    ),
    TID1 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("conv2Clusters"),
        useRingSlector = cms.bool(True),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TID2 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("conv2Clusters"),
        useRingSlector = cms.bool(True),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TID3 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("conv2Clusters"),
        useRingSlector = cms.bool(True),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TOB1 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        skipClusters = cms.InputTag("conv2Clusters")
    ),
    TOB2 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        skipClusters = cms.InputTag("conv2Clusters")
    ),
    TOB3 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        skipClusters = cms.InputTag("conv2Clusters")
    ),
    TOB4 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        skipClusters = cms.InputTag("conv2Clusters")
    ),
    TOB5 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        skipClusters = cms.InputTag("conv2Clusters")
    ),
    TOB6 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        skipClusters = cms.InputTag("conv2Clusters")
    ),
    layerList = cms.vstring(
        'BPix1+BPix2', 
        'BPix2+BPix3', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg', 
        'BPix3+TIB1', 
        'TIB1+TID1_pos', 
        'TIB1+TID1_neg', 
        'TIB1+TID2_pos', 
        'TIB1+TID2_neg', 
        'TIB1+TIB2', 
        'TIB2+TID1_pos', 
        'TIB2+TID1_neg', 
        'TIB2+TID2_pos', 
        'TIB2+TID2_neg', 
        'TIB2+TIB3', 
        'TIB3+TIB4', 
        'TIB3+TID1_pos', 
        'TIB3+TID1_neg', 
        'TIB4+TOB1', 
        'TOB1+TOB2', 
        'TOB1+TEC1_pos', 
        'TOB1+TEC1_neg', 
        'TOB2+TOB3', 
        'TOB2+TEC1_pos', 
        'TOB2+TEC1_neg', 
        'TOB3+TOB4', 
        'TOB3+TEC1_pos', 
        'TOB3+TEC1_neg', 
        'TOB4+TOB5', 
        'TOB5+TOB6', 
        'TID1_pos+TID2_pos', 
        'TID2_pos+TID3_pos', 
        'TID3_pos+TEC1_pos', 
        'TID1_neg+TID2_neg', 
        'TID2_neg+TID3_neg', 
        'TID3_neg+TEC1_neg', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TEC3_pos+TEC4_pos', 
        'TEC4_pos+TEC5_pos', 
        'TEC5_pos+TEC6_pos', 
        'TEC6_pos+TEC7_pos', 
        'TEC7_pos+TEC8_pos', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg', 
        'TEC3_neg+TEC4_neg', 
        'TEC4_neg+TEC5_neg', 
        'TEC5_neg+TEC6_neg', 
        'TEC6_neg+TEC7_neg', 
        'TEC7_neg+TEC8_neg'
    )
)


process.conv2StepSelector = cms.EDProducer("MultiTrackSelector",
    beamspot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("conv2StepTracks"),
    trackSelectors = cms.VPSet(
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(False),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(3.0),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(5.0, 8.0),
            d0_par2 = cms.vdouble(5.0, 8.0),
            dz_par1 = cms.vdouble(5.0, 8.0),
            dz_par2 = cms.vdouble(5.0, 8.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(1),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('conv2StepLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(2.5),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(5.0, 8.0),
            d0_par2 = cms.vdouble(5.0, 8.0),
            dz_par1 = cms.vdouble(5.0, 8.0),
            dz_par2 = cms.vdouble(5.0, 8.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(1),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('conv2StepTight'),
            preFilterName = cms.string('conv2StepLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(2.0),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(5.0, 8.0),
            d0_par2 = cms.vdouble(5.0, 8.0),
            dz_par1 = cms.vdouble(5.0, 8.0),
            dz_par2 = cms.vdouble(5.0, 8.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(1),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('conv2Step'),
            preFilterName = cms.string('conv2StepTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        )
    ),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.conv2StepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('conversionStep'),
    Fitter = cms.string('conv2StepFitterSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("conv2TrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.conv2TrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('conv2CkfTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("photonConvTrajSeedFromQuadruplets","conv2SeedCandidates"),
    useHitsSplitting = cms.bool(True)
)


process.convClusters = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(30.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag("tobTecStepClusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trackClassifier = cms.InputTag("tobTecStep","QualityMasks"),
    trajectories = cms.InputTag("tobTecStepTracks")
)


process.convLayerPairs = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("convClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("convClusters")
    ),
    MTIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        skipClusters = cms.InputTag("convClusters")
    ),
    MTOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        skipClusters = cms.InputTag("convClusters")
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(1),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        skipClusters = cms.InputTag("convClusters"),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        useRingSlector = cms.bool(True),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        skipClusters = cms.InputTag("convClusters")
    ),
    TID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("convClusters"),
        useRingSlector = cms.bool(True),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        skipClusters = cms.InputTag("convClusters")
    ),
    layerList = cms.vstring(
        'BPix1+BPix2', 
        'BPix2+BPix3', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg', 
        'BPix3+TIB1', 
        'BPix3+TIB2', 
        'TIB1+TID1_pos', 
        'TIB1+TID1_neg', 
        'TIB1+TID2_pos', 
        'TIB1+TID2_neg', 
        'TIB1+TIB2', 
        'TIB1+MTIB3', 
        'TIB2+TID1_pos', 
        'TIB2+TID1_neg', 
        'TIB2+TID2_pos', 
        'TIB2+TID2_neg', 
        'TIB2+MTIB3', 
        'TIB2+MTIB4', 
        'MTIB3+MTIB4', 
        'MTIB3+TOB1', 
        'MTIB3+TID1_pos', 
        'MTIB3+TID1_neg', 
        'MTIB4+TOB1', 
        'MTIB4+TOB2', 
        'TOB1+TOB2', 
        'TOB1+MTOB3', 
        'TOB1+TEC1_pos', 
        'TOB1+TEC1_neg', 
        'TOB2+MTOB3', 
        'TOB2+MTOB4', 
        'TOB2+TEC1_pos', 
        'TOB2+TEC1_neg', 
        'TID1_pos+TID2_pos', 
        'TID2_pos+TID3_pos', 
        'TID3_pos+TEC1_pos', 
        'TID1_neg+TID2_neg', 
        'TID2_neg+TID3_neg', 
        'TID3_neg+TEC1_neg', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TEC3_pos+TEC4_pos', 
        'TEC4_pos+TEC5_pos', 
        'TEC5_pos+TEC6_pos', 
        'TEC6_pos+TEC7_pos', 
        'TEC7_pos+TEC8_pos', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg', 
        'TEC3_neg+TEC4_neg', 
        'TEC4_neg+TEC5_neg', 
        'TEC5_neg+TEC6_neg', 
        'TEC6_neg+TEC7_neg', 
        'TEC7_neg+TEC8_neg'
    )
)


process.convStepSelector = cms.EDProducer("MultiTrackSelector",
    beamspot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("convStepTracks"),
    trackSelectors = cms.VPSet(
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(False),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(3.0),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(5.0, 8.0),
            d0_par2 = cms.vdouble(5.0, 8.0),
            dz_par1 = cms.vdouble(5.0, 8.0),
            dz_par2 = cms.vdouble(5.0, 8.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(1),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('convStepLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(2.5),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(5.0, 8.0),
            d0_par2 = cms.vdouble(5.0, 8.0),
            dz_par1 = cms.vdouble(5.0, 8.0),
            dz_par2 = cms.vdouble(5.0, 8.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(1),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('convStepTight'),
            preFilterName = cms.string('convStepLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(2.0),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(5.0, 8.0),
            d0_par2 = cms.vdouble(5.0, 8.0),
            dz_par1 = cms.vdouble(5.0, 8.0),
            dz_par2 = cms.vdouble(5.0, 8.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(1),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('convStep'),
            preFilterName = cms.string('convStepTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        )
    ),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.convStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('conversionStep'),
    Fitter = cms.string('convStepFitterSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("convTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.convTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('convCkfTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("convClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("photonConvTrajSeedFromSingleLeg","convSeedCandidates"),
    useHitsSplitting = cms.bool(True)
)


process.conversionStepTracks = cms.EDProducer("TrackListMerger",
    Epsilon = cms.double(-0.001),
    FoundHitBonus = cms.double(5.0),
    LostHitPenalty = cms.double(5.0),
    MaxNormalizedChisq = cms.double(1000.0),
    MinFound = cms.int32(3),
    MinPT = cms.double(0.05),
    ShareFrac = cms.double(0.19),
    TrackProducers = cms.VInputTag(cms.InputTag("convStepTracks")),
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyMVA = cms.bool(True),
    hasSelector = cms.vint32(1),
    indivShareFrac = cms.vdouble(1.0, 1.0),
    makeReKeyedSeeds = cms.untracked.bool(False),
    newQuality = cms.string('confirmed'),
    selectedTrackQuals = cms.VInputTag(cms.InputTag("convStepSelector","convStep")),
    setsToMerge = cms.VPSet(cms.PSet(
        pQual = cms.bool(True),
        tLists = cms.vint32(1)
    )),
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
    writeOnlyTrkQuals = cms.bool(False)
)


process.cosmicCandidateFinder = cms.EDProducer("CosmicTrackFinder",
    Chi2Cut = cms.double(30.0),
    GeometricStructure = cms.untracked.string('MTCC'),
    HitProducer = cms.string('siStripRecHits'),
    MinHits = cms.int32(4),
    TTRHBuilder = cms.string('WithTrackAngle'),
    cosmicSeeds = cms.InputTag("cosmicseedfinder"),
    debug = cms.untracked.bool(True),
    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
    pixelRecHits = cms.InputTag("siPixelRecHits"),
    rphirecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    stereorecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHit"),
    useHitsSplitting = cms.bool(True)
)


process.cosmicCandidateFinderP5 = cms.EDProducer("CosmicTrackFinder",
    Chi2Cut = cms.double(30.0),
    GeometricStructure = cms.untracked.string('STANDARD'),
    HitProducer = cms.string('siStripRecHits'),
    MinHits = cms.int32(4),
    TTRHBuilder = cms.string('WithTrackAngle'),
    cosmicSeeds = cms.InputTag("cosmicseedfinderP5"),
    debug = cms.untracked.bool(True),
    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
    pixelRecHits = cms.InputTag("siPixelRecHits"),
    rphirecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    stereorecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHit"),
    useHitsSplitting = cms.bool(True)
)


process.cosmicCandidateFinderP5Bottom = cms.EDProducer("CosmicTrackFinder",
    Chi2Cut = cms.double(30.0),
    GeometricStructure = cms.untracked.string('STANDARD'),
    HitProducer = cms.string('siStripRecHitsBottom'),
    MinHits = cms.int32(4),
    TTRHBuilder = cms.string('WithTrackAngle'),
    cosmicSeeds = cms.InputTag("cosmicseedfinderP5Bottom"),
    debug = cms.untracked.bool(True),
    matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
    pixelRecHits = cms.InputTag("siPixelRecHitsBottom"),
    rphirecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
    stereorecHits = cms.InputTag("siStripMatchedRecHitsBottom","stereoRecHit"),
    useHitsSplitting = cms.bool(True)
)


process.cosmicCandidateFinderP5Top = cms.EDProducer("CosmicTrackFinder",
    Chi2Cut = cms.double(30.0),
    GeometricStructure = cms.untracked.string('STANDARD'),
    HitProducer = cms.string('siStripRecHitsTop'),
    MinHits = cms.int32(4),
    TTRHBuilder = cms.string('WithTrackAngle'),
    cosmicSeeds = cms.InputTag("cosmicseedfinderP5Top"),
    debug = cms.untracked.bool(True),
    matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
    pixelRecHits = cms.InputTag("siPixelRecHitsTop"),
    rphirecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
    stereorecHits = cms.InputTag("siStripMatchedRecHitsTop","stereoRecHit"),
    useHitsSplitting = cms.bool(True)
)


process.cosmicDCCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('CosmicNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('GroupedCkfTrajectoryBuilderP5')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("cosmicDCSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.cosmicDCSeeds = cms.EDProducer("OutsideInMuonSeeder",
    cut = cms.string('pt > 2 && abs(eta)<1.2 && phi<0'),
    debug = cms.untracked.bool(False),
    errorRescaleFactor = cms.double(2.0),
    fromVertex = cms.bool(False),
    hitCollector = cms.string('hitCollectorForCosmicDCSeeds'),
    hitsToTry = cms.int32(3),
    layersToTry = cms.int32(3),
    maxEtaForTOB = cms.double(1.5),
    minEtaForTEC = cms.double(0.7),
    muonPropagator = cms.string('SteppingHelixPropagatorAlong'),
    src = cms.InputTag("muonsFromCosmics"),
    trackerPropagator = cms.string('PropagatorWithMaterial')
)


process.cosmicDCTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('ctf'),
    Fitter = cms.string('FittingSmootherRKP5'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("cosmicDCCkfTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.cosmicTrackSplitter = cms.EDProducer("CosmicTrackSplitter",
    detsToIgnore = cms.vuint32(),
    dxyCut = cms.double(9999.0),
    dzCut = cms.double(9999.0),
    excludePixelHits = cms.bool(False),
    minimumHits = cms.uint32(6),
    replaceWithInactiveHits = cms.bool(False),
    stripAllInvalidHits = cms.bool(False),
    stripBackInvalidHits = cms.bool(True),
    stripFrontInvalidHits = cms.bool(True),
    tjTkAssociationMapTag = cms.InputTag("cosmictrackfinderCosmics"),
    tracks = cms.InputTag("cosmictrackfinderCosmics")
)


process.cosmicseedfinder = cms.EDProducer("CosmicSeedGenerator",
    ClusterCollectionLabel = cms.InputTag("siStripClusters"),
    DontCountDetsAboveNClusters = cms.uint32(20),
    GeometricStructure = cms.untracked.string('STANDARD'),
    HitsForSeeds = cms.untracked.string('pairs'),
    MaxNumberOfCosmicClusters = cms.uint32(300),
    MaxNumberOfPixelClusters = cms.uint32(300),
    NegativeYOnly = cms.bool(False),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    PositiveYOnly = cms.bool(False),
    SeedPt = cms.double(5.0),
    TTRHBuilder = cms.string('WithTrackAngle'),
    doClusterCheck = cms.bool(True),
    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
    maxSeeds = cms.int32(10000),
    originHalfLength = cms.double(90.0),
    originRadius = cms.double(150.0),
    originZPosition = cms.double(0.0),
    ptMin = cms.double(0.9),
    rphirecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    stereorecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHit")
)


process.cosmicseedfinderP5 = cms.EDProducer("CosmicSeedGenerator",
    ClusterCollectionLabel = cms.InputTag("siStripClusters"),
    DontCountDetsAboveNClusters = cms.uint32(20),
    GeometricStructure = cms.untracked.string('STANDARD'),
    HitsForSeeds = cms.untracked.string('pairs'),
    MaxNumberOfCosmicClusters = cms.uint32(300),
    MaxNumberOfPixelClusters = cms.uint32(300),
    NegativeYOnly = cms.bool(False),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    PositiveYOnly = cms.bool(False),
    SeedPt = cms.double(5.0),
    TTRHBuilder = cms.string('WithTrackAngle'),
    doClusterCheck = cms.bool(True),
    matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
    maxSeeds = cms.int32(10000),
    originHalfLength = cms.double(90.0),
    originRadius = cms.double(150.0),
    originZPosition = cms.double(0.0),
    ptMin = cms.double(0.9),
    rphirecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    stereorecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHit")
)


process.cosmicseedfinderP5Bottom = cms.EDProducer("CosmicSeedGenerator",
    ClusterCollectionLabel = cms.InputTag("siStripClustersBottom"),
    DontCountDetsAboveNClusters = cms.uint32(20),
    GeometricStructure = cms.untracked.string('STANDARD'),
    HitsForSeeds = cms.untracked.string('pairs'),
    MaxNumberOfCosmicClusters = cms.uint32(150),
    MaxNumberOfPixelClusters = cms.uint32(300),
    NegativeYOnly = cms.bool(True),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    PositiveYOnly = cms.bool(False),
    SeedPt = cms.double(5.0),
    TTRHBuilder = cms.string('WithTrackAngle'),
    doClusterCheck = cms.bool(True),
    matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
    maxSeeds = cms.int32(10000),
    originHalfLength = cms.double(90.0),
    originRadius = cms.double(150.0),
    originZPosition = cms.double(0.0),
    ptMin = cms.double(0.9),
    rphirecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
    stereorecHits = cms.InputTag("siStripMatchedRecHitsBottom","stereoRecHit")
)


process.cosmicseedfinderP5Top = cms.EDProducer("CosmicSeedGenerator",
    ClusterCollectionLabel = cms.InputTag("siStripClustersTop"),
    DontCountDetsAboveNClusters = cms.uint32(20),
    GeometricStructure = cms.untracked.string('STANDARD'),
    HitsForSeeds = cms.untracked.string('pairs'),
    MaxNumberOfCosmicClusters = cms.uint32(150),
    MaxNumberOfPixelClusters = cms.uint32(300),
    NegativeYOnly = cms.bool(False),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    PositiveYOnly = cms.bool(True),
    SeedPt = cms.double(5.0),
    TTRHBuilder = cms.string('WithTrackAngle'),
    doClusterCheck = cms.bool(True),
    matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
    maxSeeds = cms.int32(10000),
    originHalfLength = cms.double(90.0),
    originRadius = cms.double(150.0),
    originZPosition = cms.double(0.0),
    ptMin = cms.double(0.9),
    rphirecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
    stereorecHits = cms.InputTag("siStripMatchedRecHitsTop","stereoRecHit")
)


process.cosmictrackfinderCosmics = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('cosmic'),
    Fitter = cms.string('RKFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    TrajectoryInEvent = cms.bool(True),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("cosmicCandidateFinderP5"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.cosmictrackfinderP5 = cms.EDProducer("CosmicTrackSelector",
    beamspot = cms.InputTag("offlineBeamSpot"),
    chi2n_par = cms.double(10.0),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    keepAllTracks = cms.bool(False),
    maxNumberLostLayers = cms.uint32(999),
    max_d0 = cms.double(110.0),
    max_eta = cms.double(2.0),
    max_z0 = cms.double(300.0),
    minNumber3DLayers = cms.uint32(0),
    minNumberLayers = cms.uint32(0),
    min_nHit = cms.uint32(5),
    min_nPixelHit = cms.uint32(0),
    min_pt = cms.double(1.0),
    qualityBit = cms.string(''),
    src = cms.InputTag("cosmictrackfinderCosmics")
)


process.cosmictrackfinderP5Bottom = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('cosmic'),
    Fitter = cms.string('RKFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    TrajectoryInEvent = cms.bool(True),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag("topBottomClusterInfoProducerBottom"),
    src = cms.InputTag("cosmicCandidateFinderP5Bottom"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.cosmictrackfinderP5Top = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('cosmic'),
    Fitter = cms.string('RKFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    TrajectoryInEvent = cms.bool(True),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag("topBottomClusterInfoProducerTop"),
    src = cms.InputTag("cosmicCandidateFinderP5Top"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.ctfCombinedSeeds = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('undefAlgorithm'),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("ckfTrackCandidatesCombinedSeeds"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.ctfNoOverlaps = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('undefAlgorithm'),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("ckfTrackCandidatesNoOverlaps"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.ctfPixelLess = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('undefAlgorithm'),
    Fitter = cms.string('RKFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("ckfTrackCandidatesPixelLess"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.ctfWithMaterialTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('undefAlgorithm'),
    Fitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("ckfTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.ctfWithMaterialTracksCosmics = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('ctf'),
    Fitter = cms.string('FittingSmootherRKP5'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("ckfTrackCandidatesP5"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.ctfWithMaterialTracksP5 = cms.EDProducer("CosmicTrackSelector",
    beamspot = cms.InputTag("offlineBeamSpot"),
    chi2n_par = cms.double(10.0),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    keepAllTracks = cms.bool(False),
    maxNumberLostLayers = cms.uint32(999),
    max_d0 = cms.double(110.0),
    max_eta = cms.double(2.0),
    max_z0 = cms.double(300.0),
    minNumber3DLayers = cms.uint32(0),
    minNumberLayers = cms.uint32(0),
    min_nHit = cms.uint32(5),
    min_nPixelHit = cms.uint32(0),
    min_pt = cms.double(1.0),
    qualityBit = cms.string(''),
    src = cms.InputTag("ctfWithMaterialTracksCosmics")
)


process.ctfWithMaterialTracksP5Bottom = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('ctf'),
    Fitter = cms.string('FittingSmootherRKP5'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag("topBottomClusterInfoProducerBottom"),
    src = cms.InputTag("ckfTrackCandidatesP5Bottom"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.ctfWithMaterialTracksP5LHCNavigation = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('ctf'),
    Fitter = cms.string('FittingSmootherRKP5'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("ckfTrackCandidatesP5LHCNavigation"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.ctfWithMaterialTracksP5Top = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('ctf'),
    Fitter = cms.string('FittingSmootherRKP5'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag("topBottomClusterInfoProducerTop"),
    src = cms.InputTag("ckfTrackCandidatesP5Top"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.dedxDiscrimASmi = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(False),
    UseStrip = cms.bool(True),
    calibrationPath = cms.string(''),
    estimator = cms.string('asmirnovDiscrim'),
    exponent = cms.double(-2.0),
    fraction = cms.double(0.4),
    tracks = cms.InputTag("generalTracks")
)


process.dedxDiscrimASmiCTF = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(False),
    UseStrip = cms.bool(True),
    calibrationPath = cms.string(''),
    estimator = cms.string('asmirnovDiscrim'),
    exponent = cms.double(-2.0),
    fraction = cms.double(0.4),
    tracks = cms.InputTag("ctfWithMaterialTracksP5")
)


process.dedxDiscrimASmiCTFP5LHC = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(False),
    UseStrip = cms.bool(True),
    calibrationPath = cms.string(''),
    estimator = cms.string('asmirnovDiscrim'),
    exponent = cms.double(-2.0),
    fraction = cms.double(0.4),
    tracks = cms.InputTag("ctfWithMaterialTracksP5LHCNavigation")
)


process.dedxDiscrimASmiCosmicTF = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(False),
    UseStrip = cms.bool(True),
    calibrationPath = cms.string(''),
    estimator = cms.string('asmirnovDiscrim'),
    exponent = cms.double(-2.0),
    fraction = cms.double(0.4),
    tracks = cms.InputTag("cosmictrackfinderP5")
)


process.dedxDiscrimBTag = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(False),
    UseStrip = cms.bool(True),
    calibrationPath = cms.string(''),
    estimator = cms.string('btagDiscrim'),
    exponent = cms.double(-2.0),
    fraction = cms.double(0.4),
    tracks = cms.InputTag("generalTracks")
)


process.dedxDiscrimProd = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(False),
    UseStrip = cms.bool(True),
    calibrationPath = cms.string(''),
    estimator = cms.string('productDiscrim'),
    exponent = cms.double(-2.0),
    fraction = cms.double(0.4),
    tracks = cms.InputTag("generalTracks")
)


process.dedxDiscrimSmi = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(False),
    UseStrip = cms.bool(True),
    calibrationPath = cms.string(''),
    estimator = cms.string('smirnovDiscrim'),
    exponent = cms.double(-2.0),
    fraction = cms.double(0.4),
    tracks = cms.InputTag("generalTracks")
)


process.dedxHarmonic2 = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(False),
    UseStrip = cms.bool(True),
    calibrationPath = cms.string(''),
    estimator = cms.string('generic'),
    exponent = cms.double(-2.0),
    fraction = cms.double(0.4),
    tracks = cms.InputTag("generalTracks")
)


process.dedxHarmonic2CTF = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(False),
    UseStrip = cms.bool(True),
    calibrationPath = cms.string(''),
    estimator = cms.string('generic'),
    exponent = cms.double(-2.0),
    fraction = cms.double(0.4),
    tracks = cms.InputTag("ctfWithMaterialTracksP5")
)


process.dedxHarmonic2CTFP5LHC = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(False),
    UseStrip = cms.bool(True),
    calibrationPath = cms.string(''),
    estimator = cms.string('generic'),
    exponent = cms.double(-2.0),
    fraction = cms.double(0.4),
    tracks = cms.InputTag("ctfWithMaterialTracksP5LHCNavigation")
)


process.dedxHarmonic2CosmicTF = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(False),
    UseStrip = cms.bool(True),
    calibrationPath = cms.string(''),
    estimator = cms.string('generic'),
    exponent = cms.double(-2.0),
    fraction = cms.double(0.4),
    tracks = cms.InputTag("cosmictrackfinderP5")
)


process.dedxHitInfo = cms.EDProducer("DeDxHitInfoProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    calibrationPath = cms.string('file:Gains.root'),
    lowPtTracksDeDxThreshold = cms.double(3.5),
    lowPtTracksEstimatorParameters = cms.PSet(
        exponent = cms.double(-2.0),
        fraction = cms.double(-0.15)
    ),
    lowPtTracksPrescaleFail = cms.uint32(2000),
    lowPtTracksPrescalePass = cms.uint32(100),
    maxTrackEta = cms.double(5.0),
    minTrackHits = cms.uint32(0),
    minTrackPt = cms.double(10),
    minTrackPtPrescale = cms.double(0.5),
    shapeTest = cms.bool(True),
    tracks = cms.InputTag("generalTracks"),
    useCalibration = cms.bool(False),
    usePixel = cms.bool(True),
    useStrip = cms.bool(True)
)


process.dedxHitInfoCTF = cms.EDProducer("DeDxHitInfoProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    calibrationPath = cms.string('file:Gains.root'),
    lowPtTracksDeDxThreshold = cms.double(3.5),
    lowPtTracksEstimatorParameters = cms.PSet(
        exponent = cms.double(-2.0),
        fraction = cms.double(-0.15)
    ),
    lowPtTracksPrescaleFail = cms.uint32(2000),
    lowPtTracksPrescalePass = cms.uint32(100),
    maxTrackEta = cms.double(5.0),
    minTrackHits = cms.uint32(0),
    minTrackPt = cms.double(10),
    minTrackPtPrescale = cms.double(0.5),
    shapeTest = cms.bool(True),
    tracks = cms.InputTag("ctfWithMaterialTracksP5"),
    useCalibration = cms.bool(False),
    usePixel = cms.bool(True),
    useStrip = cms.bool(True)
)


process.dedxHitInfoCTFP5LHC = cms.EDProducer("DeDxHitInfoProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    calibrationPath = cms.string('file:Gains.root'),
    lowPtTracksDeDxThreshold = cms.double(3.5),
    lowPtTracksEstimatorParameters = cms.PSet(
        exponent = cms.double(-2.0),
        fraction = cms.double(-0.15)
    ),
    lowPtTracksPrescaleFail = cms.uint32(2000),
    lowPtTracksPrescalePass = cms.uint32(100),
    maxTrackEta = cms.double(5.0),
    minTrackHits = cms.uint32(0),
    minTrackPt = cms.double(10),
    minTrackPtPrescale = cms.double(0.5),
    shapeTest = cms.bool(True),
    tracks = cms.InputTag("ctfWithMaterialTracksP5LHCNavigation"),
    useCalibration = cms.bool(False),
    usePixel = cms.bool(True),
    useStrip = cms.bool(True)
)


process.dedxHitInfoCosmicTF = cms.EDProducer("DeDxHitInfoProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    calibrationPath = cms.string('file:Gains.root'),
    lowPtTracksDeDxThreshold = cms.double(3.5),
    lowPtTracksEstimatorParameters = cms.PSet(
        exponent = cms.double(-2.0),
        fraction = cms.double(-0.15)
    ),
    lowPtTracksPrescaleFail = cms.uint32(2000),
    lowPtTracksPrescalePass = cms.uint32(100),
    maxTrackEta = cms.double(5.0),
    minTrackHits = cms.uint32(0),
    minTrackPt = cms.double(10),
    minTrackPtPrescale = cms.double(0.5),
    shapeTest = cms.bool(True),
    tracks = cms.InputTag("cosmictrackfinderP5"),
    useCalibration = cms.bool(False),
    usePixel = cms.bool(True),
    useStrip = cms.bool(True)
)


process.dedxMedian = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(False),
    UseStrip = cms.bool(True),
    calibrationPath = cms.string(''),
    estimator = cms.string('median'),
    exponent = cms.double(-2.0),
    fraction = cms.double(0.4),
    tracks = cms.InputTag("generalTracks")
)


process.dedxPixelAndStripHarmonic2T085 = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(True),
    UseStrip = cms.bool(True),
    calibrationPath = cms.string(''),
    estimator = cms.string('genericTruncated'),
    exponent = cms.double(-2.0),
    fraction = cms.double(-0.15),
    tracks = cms.InputTag("generalTracks")
)


process.dedxPixelHarmonic2 = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(True),
    UseStrip = cms.bool(False),
    calibrationPath = cms.string(''),
    estimator = cms.string('generic'),
    exponent = cms.double(-2.0),
    fraction = cms.double(0.4),
    tracks = cms.InputTag("generalTracks")
)


process.dedxTruncated40 = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(False),
    UseStrip = cms.bool(True),
    calibrationPath = cms.string(''),
    estimator = cms.string('truncated'),
    exponent = cms.double(-2.0),
    fraction = cms.double(0.4),
    tracks = cms.InputTag("generalTracks")
)


process.dedxTruncated40CTF = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(False),
    UseStrip = cms.bool(True),
    calibrationPath = cms.string(''),
    estimator = cms.string('truncated'),
    exponent = cms.double(-2.0),
    fraction = cms.double(0.4),
    tracks = cms.InputTag("ctfWithMaterialTracksP5")
)


process.dedxTruncated40CTFP5LHC = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(False),
    UseStrip = cms.bool(True),
    calibrationPath = cms.string(''),
    estimator = cms.string('truncated'),
    exponent = cms.double(-2.0),
    fraction = cms.double(0.4),
    tracks = cms.InputTag("ctfWithMaterialTracksP5LHCNavigation")
)


process.dedxTruncated40CosmicTF = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(False),
    UseStrip = cms.bool(True),
    calibrationPath = cms.string(''),
    estimator = cms.string('truncated'),
    exponent = cms.double(-2.0),
    fraction = cms.double(0.4),
    tracks = cms.InputTag("cosmictrackfinderP5")
)


process.dedxUnbinned = cms.EDProducer("DeDxEstimatorProducer",
    MeVperADCPixel = cms.double(3.61e-06),
    MeVperADCStrip = cms.double(0.00095665),
    ProbabilityMode = cms.string('Accumulation'),
    Reccord = cms.string('SiStripDeDxMip_3D_Rcd'),
    ShapeTest = cms.bool(True),
    UseCalibration = cms.bool(False),
    UsePixel = cms.bool(False),
    UseStrip = cms.bool(True),
    calibrationPath = cms.string(''),
    estimator = cms.string('unbinnedFit'),
    exponent = cms.double(-2.0),
    fraction = cms.double(0.4),
    tracks = cms.InputTag("generalTracks")
)


process.detachedQuadStep = cms.EDProducer("TrackMVAClassifierDetached",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorDetachedQuadStep_Phase1')
    ),
    qualityCuts = cms.vdouble(-0.5, 0.0, 0.5),
    src = cms.InputTag("detachedQuadStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.detachedQuadStepClusters = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag(""),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trackClassifier = cms.InputTag("","QualityMasks"),
    trajectories = cms.InputTag("")
)


process.detachedQuadStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0, 1, 2),
    maxElement = cms.uint32(50000000),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("detachedQuadStepSeedLayers"),
    trackingRegions = cms.InputTag("detachedQuadStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.detachedQuadStepHitQuadruplets = cms.EDProducer("CAHitQuadrupletEDProducer",
    CAHardPtCut = cms.double(0),
    CAPhiCut = cms.double(0),
    CAThetaCut = cms.double(0.0011),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    doublets = cms.InputTag("detachedQuadStepHitDoublets"),
    extraHitRPhitolerance = cms.double(0),
    fitFastCircle = cms.bool(True),
    fitFastCircleChi2Cut = cms.bool(True),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.8),
        pt2 = cms.double(2),
        value1 = cms.double(500),
        value2 = cms.double(100)
    ),
    useBendingCorrection = cms.bool(True)
)


process.detachedQuadStepMasks = cms.EDProducer("FastTrackerRecHitMaskProducer",
    TrackQuality = cms.string('highPurity'),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    minNumberOfLayersWithMeasBeforeFiltering_ = cms.int32(0),
    oldHitRemovalInfo = cms.InputTag(""),
    recHits = cms.InputTag("fastTrackerRecHits"),
    trackClassifier = cms.InputTag("","QualityMasks"),
    trackQuality = cms.string('hightPurity'),
    trajectories = cms.InputTag("")
)


process.detachedQuadStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedQuadStepClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedQuadStepClusters")
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2+BPix3+BPix4', 
        'BPix1+BPix2+BPix3+FPix1_pos', 
        'BPix1+BPix2+BPix3+FPix1_neg', 
        'BPix1+BPix2+FPix1_pos+FPix2_pos', 
        'BPix1+BPix2+FPix1_neg+FPix2_neg', 
        'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
        'BPix1+FPix1_neg+FPix2_neg+FPix3_neg'
    )
)


process.detachedQuadStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("detachedQuadStepHitQuadruplets")
)


process.detachedQuadStepSelector = cms.EDProducer("MultiTrackSelector",
    beamspot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("detachedQuadStepTracks"),
    trackSelectors = cms.VPSet(
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(1.0),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.9, 3.0),
            d0_par2 = cms.vdouble(1.0, 3.0),
            dz_par1 = cms.vdouble(0.9, 3.0),
            dz_par2 = cms.vdouble(1.0, 3.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(999),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(0),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('detachedQuadStepVtxLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.6),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(1.3, 4.0),
            d0_par2 = cms.vdouble(1.3, 4.0),
            dz_par1 = cms.vdouble(1.3, 4.0),
            dz_par2 = cms.vdouble(1.3, 4.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(999),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(0),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('detachedQuadStepTrkLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.9),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.9, 3.0),
            d0_par2 = cms.vdouble(0.9, 3.0),
            dz_par1 = cms.vdouble(0.9, 3.0),
            dz_par2 = cms.vdouble(0.9, 3.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('detachedQuadStepVtxTight'),
            preFilterName = cms.string('detachedQuadStepVtxLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.5),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(1.1, 4.0),
            d0_par2 = cms.vdouble(1.1, 4.0),
            dz_par1 = cms.vdouble(1.1, 4.0),
            dz_par2 = cms.vdouble(1.1, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(4),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('detachedQuadStepTrkTight'),
            preFilterName = cms.string('detachedQuadStepTrkLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.9),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.8, 3.0),
            d0_par2 = cms.vdouble(0.8, 3.0),
            dz_par1 = cms.vdouble(0.8, 3.0),
            dz_par2 = cms.vdouble(0.8, 3.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('detachedQuadStepVtx'),
            preFilterName = cms.string('detachedQuadStepVtxTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.5),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.9, 4.0),
            d0_par2 = cms.vdouble(0.9, 4.0),
            dz_par1 = cms.vdouble(0.9, 4.0),
            dz_par2 = cms.vdouble(0.9, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(4),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('detachedQuadStepTrk'),
            preFilterName = cms.string('detachedQuadStepTrkTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        )
    ),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.detachedQuadStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('detachedQuadStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('detachedQuadStepTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("detachedQuadStepClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("detachedQuadStepSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.detachedQuadStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(0),
        originHalfLength = cms.double(15.0),
        originRadius = cms.double(1.5),
        precise = cms.bool(True),
        ptMin = cms.double(0.3),
        useMultipleScattering = cms.bool(False)
    )
)


process.detachedQuadStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('detachedQuadStep'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("detachedQuadStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.detachedTripletStep = cms.EDProducer("ClassifierMerger",
    inputClassifiers = cms.vstring(
        'detachedTripletStepClassifier1', 
        'detachedTripletStepClassifier2'
    )
)


process.detachedTripletStepClassifier1 = cms.EDProducer("TrackMVAClassifierDetached",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorIter3_13TeV')
    ),
    qualityCuts = cms.vdouble(-0.5, 0.0, 0.5),
    src = cms.InputTag("detachedTripletStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.detachedTripletStepClassifier2 = cms.EDProducer("TrackMVAClassifierPrompt",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorIter0_13TeV')
    ),
    qualityCuts = cms.vdouble(-0.2, 0.0, 0.4),
    src = cms.InputTag("detachedTripletStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.detachedTripletStepClusters = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag(""),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trackClassifier = cms.InputTag("initialStep","QualityMasks"),
    trajectories = cms.InputTag("initialStepTracks")
)


process.detachedTripletStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(50000000),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("detachedTripletStepSeedLayers"),
    trackingRegions = cms.InputTag("detachedTripletStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.detachedTripletStepHitTriplets = cms.EDProducer("PixelTripletLargeTipEDProducer",
    doublets = cms.InputTag("detachedTripletStepHitDoublets"),
    extraHitRPhitolerance = cms.double(0),
    extraHitRZtolerance = cms.double(0),
    maxElement = cms.uint32(1000000),
    phiPreFiltering = cms.double(0.3),
    produceIntermediateHitTriplets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    useBending = cms.bool(True),
    useFixedPreFiltering = cms.bool(False),
    useMultScattering = cms.bool(True)
)


process.detachedTripletStepMasks = cms.EDProducer("FastTrackerRecHitMaskProducer",
    TrackQuality = cms.string('highPurity'),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    minNumberOfLayersWithMeasBeforeFiltering_ = cms.int32(0),
    oldHitRemovalInfo = cms.InputTag(""),
    recHits = cms.InputTag("fastTrackerRecHits"),
    trackClassifier = cms.InputTag("initialStep","QualityMasks"),
    trackQuality = cms.string('hightPurity'),
    trajectories = cms.InputTag("initialStepTracks")
)


process.detachedTripletStepSeedClusterMask = cms.EDProducer("SeedClusterRemover",
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trajectories = cms.InputTag("lowPtTripletStepSeeds")
)


process.detachedTripletStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedTripletStepClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("detachedTripletStepClusters")
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'
    )
)


process.detachedTripletStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("detachedTripletStepHitTriplets")
)


process.detachedTripletStepSelector = cms.EDProducer("MultiTrackSelector",
    GBRForestLabel = cms.string('MVASelectorIter3'),
    beamspot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("detachedTripletStepTracks"),
    trackSelectors = cms.VPSet(
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(1.6),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(1.2, 3.0),
            d0_par2 = cms.vdouble(1.3, 3.0),
            dz_par1 = cms.vdouble(1.2, 3.0),
            dz_par2 = cms.vdouble(1.3, 3.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(999),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(0),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('detachedTripletStepVtxLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.7),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(1.6, 4.0),
            d0_par2 = cms.vdouble(1.6, 4.0),
            dz_par1 = cms.vdouble(1.6, 4.0),
            dz_par2 = cms.vdouble(1.6, 4.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(999),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(0),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('detachedTripletStepTrkLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.7),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.95, 3.0),
            d0_par2 = cms.vdouble(1.0, 3.0),
            dz_par1 = cms.vdouble(0.9, 3.0),
            dz_par2 = cms.vdouble(1.0, 3.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('detachedTripletStepVtxTight'),
            preFilterName = cms.string('detachedTripletStepVtxLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.5),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(1.1, 4.0),
            d0_par2 = cms.vdouble(1.1, 4.0),
            dz_par1 = cms.vdouble(1.1, 4.0),
            dz_par2 = cms.vdouble(1.1, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(5),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('detachedTripletStepTrkTight'),
            preFilterName = cms.string('detachedTripletStepTrkLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.7),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.85, 3.0),
            d0_par2 = cms.vdouble(0.9, 3.0),
            dz_par1 = cms.vdouble(0.8, 3.0),
            dz_par2 = cms.vdouble(0.9, 3.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('detachedTripletStepVtx'),
            preFilterName = cms.string('detachedTripletStepVtxTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.4),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(1.0, 4.0),
            d0_par2 = cms.vdouble(1.0, 4.0),
            dz_par1 = cms.vdouble(1.0, 4.0),
            dz_par2 = cms.vdouble(1.0, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(4),
            minNumberLayers = cms.uint32(5),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('detachedTripletStepTrk'),
            preFilterName = cms.string('detachedTripletStepTrkTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        )
    ),
    useAnyMVA = cms.bool(False),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.detachedTripletStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('detachedTripletStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('detachedTripletStepTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("detachedTripletStepClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("detachedTripletStepSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.detachedTripletStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(0),
        originHalfLength = cms.double(15.0),
        originRadius = cms.double(1.5),
        precise = cms.bool(True),
        ptMin = cms.double(0.3),
        useMultipleScattering = cms.bool(False)
    )
)


process.detachedTripletStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('detachedTripletStep'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("detachedTripletStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.duplicateTrackCandidates = cms.EDProducer("DuplicateTrackMerger",
    GBRForestFileName = cms.string(''),
    chi2EstimatorName = cms.string('duplicateTrackCandidatesChi2Est'),
    forestLabel = cms.string('MVADuplicate'),
    maxDCA = cms.double(30),
    maxDLambda = cms.double(0.3),
    maxDPhi = cms.double(0.3),
    maxDQoP = cms.double(0.25),
    maxDdsz = cms.double(10),
    maxDdxy = cms.double(10),
    minBDTG = cms.double(-0.1),
    minDeltaR3d = cms.double(-4),
    minP = cms.double(0.4),
    minpT = cms.double(0.2),
    overlapCheckMaxHits = cms.uint32(4),
    overlapCheckMaxMissingLayers = cms.uint32(1),
    overlapCheckMinCosT = cms.double(0.99),
    propagatorName = cms.string('PropagatorWithMaterial'),
    source = cms.InputTag("preDuplicateMergingGeneralTracks"),
    ttrhBuilderName = cms.string('WithAngleAndTemplate'),
    useInnermostState = cms.bool(True)
)


process.duplicateTrackClassifier = cms.EDProducer("TrackCutClassifier",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            drWPVerr_par = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dr_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dr_par1 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dr_par2 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38)
        ),
        dz_par = cms.PSet(
            dzWPVerr_par = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dz_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dz_par1 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dz_par2 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38)
        ),
        isHLT = cms.bool(False),
        maxChi2 = cms.vdouble(9999.0, 9999.0, 9999.0),
        maxChi2n = cms.vdouble(10.0, 1.0, 0.4),
        maxDr = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        maxDz = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24, 15),
        maxLostLayers = cms.vint32(99, 99, 99),
        maxRelPtErr = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        min3DLayers = cms.vint32(0, 0, 0),
        minHits = cms.vint32(0, 0, 1),
        minHits4pass = cms.vint32(2147483647, 2147483647, 2147483647),
        minLayers = cms.vint32(0, 0, 0),
        minNVtxTrk = cms.int32(2),
        minNdof = cms.vdouble(-1, -1, -1),
        minPixelHits = cms.vint32(0, 0, 0)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("mergedDuplicateTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.earlyGeneralTracks = cms.EDProducer("TrackCollectionMerger",
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    enableMerging = cms.bool(True),
    foundHitBonus = cms.double(10),
    inputClassifiers = cms.vstring(
        'initialStep', 
        'jetCoreRegionalStep', 
        'lowPtTripletStep', 
        'pixelPairStep', 
        'detachedTripletStep', 
        'mixedTripletStep', 
        'pixelLessStep', 
        'tobTecStep'
    ),
    lostHitPenalty = cms.double(5),
    minQuality = cms.string('loose'),
    minShareHits = cms.uint32(2),
    shareFrac = cms.double(0.19),
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
    trackProducers = cms.VInputTag(
        "initialStepTracks", "jetCoreRegionalStepTracks", "lowPtTripletStepTracks", "pixelPairStepTracks", "detachedTripletStepTracks", 
        "mixedTripletStepTracks", "pixelLessStepTracks", "tobTecStepTracks"
    )
)


process.earlyMuons = cms.EDProducer("MuonIdProducer",
    CaloExtractorPSet = cms.PSet(
        CenterConeOnCalIntersection = cms.bool(False),
        ComponentName = cms.string('CaloExtractorByAssociator'),
        DR_Max = cms.double(0.5),
        DR_Veto_E = cms.double(0.07),
        DR_Veto_H = cms.double(0.1),
        DR_Veto_HO = cms.double(0.1),
        DepositInstanceLabels = cms.vstring(
            'ecal', 
            'hcal', 
            'ho'
        ),
        DepositLabel = cms.untracked.string('Cal'),
        NoiseTow_EB = cms.double(0.04),
        NoiseTow_EE = cms.double(0.15),
        Noise_EB = cms.double(0.025),
        Noise_EE = cms.double(0.1),
        Noise_HB = cms.double(0.2),
        Noise_HE = cms.double(0.2),
        Noise_HO = cms.double(0.2),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold_E = cms.double(0.2),
        Threshold_H = cms.double(0.5),
        Threshold_HO = cms.double(0.5),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(1.0),
            dREcalPreselection = cms.double(1.0),
            dRHcal = cms.double(1.0),
            dRHcalPreselection = cms.double(1.0),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useGEM = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useME0 = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        ),
        UseRecHitsFlag = cms.bool(False)
    ),
    JetExtractorPSet = cms.PSet(
        ComponentName = cms.string('JetExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.1),
        ExcludeMuonVeto = cms.bool(True),
        JetCollectionLabel = cms.InputTag("ak4CaloJets"),
        PrintTimeReport = cms.untracked.bool(False),
        PropagatorName = cms.string('SteppingHelixPropagatorAny'),
        ServiceParameters = cms.PSet(
            Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
            RPCLayers = cms.bool(False),
            UseMuonNavigation = cms.untracked.bool(False)
        ),
        Threshold = cms.double(5.0),
        TrackAssociatorParameters = cms.PSet(
            CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
            CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
            DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
            EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
            EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
            GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
            HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
            HORecHitCollectionLabel = cms.InputTag("horeco"),
            ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
            accountForTrajectoryChangeCalo = cms.bool(False),
            dREcal = cms.double(0.5),
            dREcalPreselection = cms.double(0.5),
            dRHcal = cms.double(0.5),
            dRHcalPreselection = cms.double(0.5),
            dRMuon = cms.double(9999.0),
            dRMuonPreselection = cms.double(0.2),
            dRPreshowerPreselection = cms.double(0.2),
            muonMaxDistanceSigmaX = cms.double(0.0),
            muonMaxDistanceSigmaY = cms.double(0.0),
            muonMaxDistanceX = cms.double(5.0),
            muonMaxDistanceY = cms.double(5.0),
            propagateAllDirections = cms.bool(True),
            trajectoryUncertaintyTolerance = cms.double(-1.0),
            truthMatch = cms.bool(False),
            useCalo = cms.bool(True),
            useEcal = cms.bool(False),
            useGEM = cms.bool(False),
            useHO = cms.bool(False),
            useHcal = cms.bool(False),
            useME0 = cms.bool(False),
            useMuon = cms.bool(False),
            usePreshower = cms.bool(False)
        )
    ),
    MuonCaloCompatibility = cms.PSet(
        MuonTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root'),
        PionTemplateFileName = cms.FileInPath('RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root'),
        allSiPMHO = cms.bool(False),
        delta_eta = cms.double(0.02),
        delta_phi = cms.double(0.02)
    ),
    ShowerDigiFillerParameters = cms.PSet(
        cscDigiCollectionLabel = cms.InputTag("muonCSCDigis","MuonCSCStripDigi"),
        digiMaxDistanceX = cms.double(25.0),
        dtDigiCollectionLabel = cms.InputTag("muonDTDigis")
    ),
    TimingFillerParameters = cms.PSet(
        CSCTimingParameters = cms.PSet(
            CSCStripError = cms.double(7.0),
            CSCStripTimeOffset = cms.double(0.0),
            CSCWireError = cms.double(8.6),
            CSCWireTimeOffset = cms.double(0.0),
            PruneCut = cms.double(9.0),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring(
                    'SteppingHelixPropagatorAny', 
                    'PropagatorWithMaterial', 
                    'PropagatorWithMaterialOpposite'
                ),
                RPCLayers = cms.bool(True)
            ),
            UseStripTime = cms.bool(True),
            UseWireTime = cms.bool(True),
            debug = cms.bool(False)
        ),
        DTTimingParameters = cms.PSet(
            DTTimeOffset = cms.double(0.0),
            DoWireCorr = cms.bool(True),
            DropTheta = cms.bool(True),
            HitError = cms.double(2.8),
            HitsMin = cms.int32(3),
            PruneCut = cms.double(5.0),
            RequireBothProjections = cms.bool(False),
            ServiceParameters = cms.PSet(
                Propagators = cms.untracked.vstring(
                    'SteppingHelixPropagatorAny', 
                    'PropagatorWithMaterial', 
                    'PropagatorWithMaterialOpposite'
                ),
                RPCLayers = cms.bool(True)
            ),
            UseSegmentT0 = cms.bool(False),
            debug = cms.bool(False)
        ),
        EcalEnergyCut = cms.double(0.4),
        ErrorEB = cms.double(2.085),
        ErrorEE = cms.double(6.95),
        MatchParameters = cms.PSet(
            CSCsegments = cms.InputTag("cscSegments"),
            DTradius = cms.double(0.01),
            DTsegments = cms.InputTag("dt4DSegments"),
            RPChits = cms.InputTag("rpcRecHits"),
            TightMatchCSC = cms.bool(True),
            TightMatchDT = cms.bool(False)
        ),
        UseCSC = cms.bool(True),
        UseDT = cms.bool(True),
        UseECAL = cms.bool(False)
    ),
    TrackAssociatorParameters = cms.PSet(
        CSCSegmentCollectionLabel = cms.InputTag("cscSegments"),
        CaloTowerCollectionLabel = cms.InputTag("towerMaker"),
        DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments"),
        EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
        EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
        GEMSegmentCollectionLabel = cms.InputTag("gemSegments"),
        HBHERecHitCollectionLabel = cms.InputTag("hbhereco"),
        HORecHitCollectionLabel = cms.InputTag("horeco"),
        ME0SegmentCollectionLabel = cms.InputTag("me0Segments"),
        accountForTrajectoryChangeCalo = cms.bool(False),
        dREcal = cms.double(9999.0),
        dREcalPreselection = cms.double(0.05),
        dRHcal = cms.double(9999.0),
        dRHcalPreselection = cms.double(0.2),
        dRMuon = cms.double(9999.0),
        dRMuonPreselection = cms.double(0.2),
        dRPreshowerPreselection = cms.double(0.2),
        muonMaxDistanceSigmaX = cms.double(0.0),
        muonMaxDistanceSigmaY = cms.double(0.0),
        muonMaxDistanceX = cms.double(5.0),
        muonMaxDistanceY = cms.double(5.0),
        propagateAllDirections = cms.bool(True),
        trajectoryUncertaintyTolerance = cms.double(-1.0),
        truthMatch = cms.bool(False),
        useCalo = cms.bool(False),
        useEcal = cms.bool(False),
        useGEM = cms.bool(False),
        useHO = cms.bool(False),
        useHcal = cms.bool(False),
        useME0 = cms.bool(False),
        useMuon = cms.bool(True),
        usePreshower = cms.bool(False)
    ),
    TrackExtractorPSet = cms.PSet(
        BeamSpotLabel = cms.InputTag("offlineBeamSpot"),
        BeamlineOption = cms.string('BeamSpotFromEvent'),
        Chi2Ndof_Max = cms.double(1e+64),
        Chi2Prob_Min = cms.double(-1.0),
        ComponentName = cms.string('TrackExtractor'),
        DR_Max = cms.double(0.5),
        DR_Veto = cms.double(0.01),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        NHits_Min = cms.uint32(0),
        Pt_Min = cms.double(-1.0),
        inputTrackCollection = cms.InputTag("generalTracks")
    ),
    TrackerKinkFinderParameters = cms.PSet(
        DoPredictionsOnly = cms.bool(False),
        Fitter = cms.string('KFFitterForRefitInsideOut'),
        MTDRecHitBuilder = cms.string('MTDRecHitBuilder'),
        MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
        Propagator = cms.string('SmartPropagatorAnyRKOpposite'),
        RefitDirection = cms.string('alongMomentum'),
        RefitRPCHits = cms.bool(True),
        Smoother = cms.string('KFSmootherForRefitInsideOut'),
        TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
        diagonalOnly = cms.bool(False),
        usePosition = cms.bool(True)
    ),
    addExtraSoftMuons = cms.bool(False),
    arbitrateTrackerMuons = cms.bool(True),
    arbitrationCleanerOptions = cms.PSet(
        ClusterDPhi = cms.double(0.6),
        ClusterDTheta = cms.double(0.02),
        Clustering = cms.bool(True),
        ME1a = cms.bool(True),
        Overlap = cms.bool(True),
        OverlapDPhi = cms.double(0.0786),
        OverlapDTheta = cms.double(0.02)
    ),
    debugWithTruthMatching = cms.bool(False),
    ecalDepositName = cms.string('ecal'),
    fillCaloCompatibility = cms.bool(False),
    fillEnergy = cms.bool(False),
    fillGlobalTrackQuality = cms.bool(False),
    fillGlobalTrackRefits = cms.bool(False),
    fillIsolation = cms.bool(False),
    fillMatching = cms.bool(True),
    fillShowerDigis = cms.bool(True),
    fillTrackerKink = cms.bool(False),
    globalTrackQualityInputTag = cms.InputTag("glbTrackQual"),
    hcalDepositName = cms.string('hcal'),
    hoDepositName = cms.string('ho'),
    inputCollectionLabels = cms.VInputTag(cms.InputTag("earlyGeneralTracks"), cms.InputTag("standAloneMuons","UpdatedAtVtx")),
    inputCollectionTypes = cms.vstring(
        'inner tracks', 
        'outer tracks'
    ),
    jetDepositName = cms.string('jets'),
    maxAbsDx = cms.double(3.0),
    maxAbsDy = cms.double(9999.0),
    maxAbsEta = cms.double(3.0),
    maxAbsPullX = cms.double(3.0),
    maxAbsPullY = cms.double(9999.0),
    minCaloCompatibility = cms.double(0.6),
    minNumberOfMatches = cms.int32(1),
    minP = cms.double(3.0),
    minPCaloMuon = cms.double(3.0),
    minPt = cms.double(2.0),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double(200.0),
    runArbitrationCleaner = cms.bool(True),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double(2.0),
    storeCrossedHcalRecHits = cms.bool(True),
    trackDepositName = cms.string('tracker'),
    writeIsoDeposits = cms.bool(True)
)


process.firstStepPrimaryVertices = cms.EDProducer("RecoChargedRefCandidatePrimaryVertexSorter",
    assignment = cms.PSet(
        maxDistanceToJetAxis = cms.double(0.07),
        maxDtSigForPrimaryAssignment = cms.double(4.0),
        maxDxyForJetAxisAssigment = cms.double(0.1),
        maxDxyForNotReconstructedPrimary = cms.double(0.01),
        maxDxySigForNotReconstructedPrimary = cms.double(2),
        maxDzErrorForPrimaryAssignment = cms.double(0.05),
        maxDzForJetAxisAssigment = cms.double(0.1),
        maxDzForPrimaryAssignment = cms.double(0.1),
        maxDzSigForPrimaryAssignment = cms.double(5.0),
        maxJetDeltaR = cms.double(0.5),
        minJetPt = cms.double(25),
        preferHighRanked = cms.bool(False),
        useTiming = cms.bool(False)
    ),
    jets = cms.InputTag("ak4CaloJetsForTrk"),
    particles = cms.InputTag("initialStepTrackRefsForJets"),
    produceAssociationToOriginalVertices = cms.bool(False),
    produceNoPileUpCollection = cms.bool(False),
    producePileUpCollection = cms.bool(False),
    produceSortedVertices = cms.bool(True),
    qualityForPrimary = cms.int32(3),
    sorting = cms.PSet(

    ),
    trackTimeResoTag = cms.InputTag(""),
    trackTimeTag = cms.InputTag(""),
    usePVMET = cms.bool(True),
    vertices = cms.InputTag("firstStepPrimaryVerticesUnsorted")
)


process.firstStepPrimaryVerticesBeforeMixing = cms.EDProducer("PrimaryVertexProducer",
    TkClusParameters = cms.PSet(
        TkDAClusParameters = cms.PSet(
            Tmin = cms.double(2.0),
            Tpurge = cms.double(2.0),
            Tstop = cms.double(0.5),
            coolingFactor = cms.double(0.6),
            d0CutOff = cms.double(3.0),
            dzCutOff = cms.double(3.0),
            uniquetrkweight = cms.double(0.8),
            vertexSize = cms.double(0.006),
            zmerge = cms.double(0.01)
        ),
        algorithm = cms.string('DA_vect')
    ),
    TkFilterParameters = cms.PSet(
        algorithm = cms.string('filter'),
        maxD0Significance = cms.double(4.0),
        maxEta = cms.double(2.4),
        maxNormalizedChi2 = cms.double(10.0),
        minPixelLayersWithHits = cms.int32(2),
        minPt = cms.double(0.0),
        minSiliconLayersWithHits = cms.int32(5),
        trackQuality = cms.string('any')
    ),
    TrackLabel = cms.InputTag("initialStepTracks"),
    beamSpotLabel = cms.InputTag("offlineBeamSpot"),
    verbose = cms.untracked.bool(False),
    vertexCollections = cms.VPSet(cms.PSet(
        algorithm = cms.string('AdaptiveVertexFitter'),
        chi2cutoff = cms.double(2.5),
        label = cms.string(''),
        maxDistanceToBeam = cms.double(1.0),
        minNdof = cms.double(0.0),
        useBeamConstraint = cms.bool(False)
    ))
)


process.firstStepPrimaryVerticesPreSplitting = cms.EDProducer("PrimaryVertexProducer",
    TkClusParameters = cms.PSet(
        TkDAClusParameters = cms.PSet(
            Tmin = cms.double(2.0),
            Tpurge = cms.double(2.0),
            Tstop = cms.double(0.5),
            coolingFactor = cms.double(0.6),
            d0CutOff = cms.double(3.0),
            dzCutOff = cms.double(3.0),
            uniquetrkweight = cms.double(0.8),
            vertexSize = cms.double(0.006),
            zmerge = cms.double(0.01)
        ),
        algorithm = cms.string('DA_vect')
    ),
    TkFilterParameters = cms.PSet(
        algorithm = cms.string('filter'),
        maxD0Significance = cms.double(4.0),
        maxEta = cms.double(2.4),
        maxNormalizedChi2 = cms.double(10.0),
        minPixelLayersWithHits = cms.int32(2),
        minPt = cms.double(0.0),
        minSiliconLayersWithHits = cms.int32(5),
        trackQuality = cms.string('any')
    ),
    TrackLabel = cms.InputTag("initialStepTracksPreSplitting"),
    beamSpotLabel = cms.InputTag("offlineBeamSpot"),
    verbose = cms.untracked.bool(False),
    vertexCollections = cms.VPSet(cms.PSet(
        algorithm = cms.string('AdaptiveVertexFitter'),
        chi2cutoff = cms.double(2.5),
        label = cms.string(''),
        maxDistanceToBeam = cms.double(1.0),
        minNdof = cms.double(0.0),
        useBeamConstraint = cms.bool(False)
    ))
)


process.firstStepPrimaryVerticesUnsorted = cms.EDProducer("PrimaryVertexProducer",
    TkClusParameters = cms.PSet(
        TkDAClusParameters = cms.PSet(
            Tmin = cms.double(2.0),
            Tpurge = cms.double(2.0),
            Tstop = cms.double(0.5),
            coolingFactor = cms.double(0.6),
            d0CutOff = cms.double(3.0),
            dzCutOff = cms.double(3.0),
            uniquetrkweight = cms.double(0.8),
            vertexSize = cms.double(0.006),
            zmerge = cms.double(0.01)
        ),
        algorithm = cms.string('DA_vect')
    ),
    TkFilterParameters = cms.PSet(
        algorithm = cms.string('filter'),
        maxD0Significance = cms.double(4.0),
        maxEta = cms.double(2.4),
        maxNormalizedChi2 = cms.double(10.0),
        minPixelLayersWithHits = cms.int32(2),
        minPt = cms.double(0.0),
        minSiliconLayersWithHits = cms.int32(5),
        trackQuality = cms.string('any')
    ),
    TrackLabel = cms.InputTag("initialStepTracks"),
    beamSpotLabel = cms.InputTag("offlineBeamSpot"),
    verbose = cms.untracked.bool(False),
    vertexCollections = cms.VPSet(cms.PSet(
        algorithm = cms.string('AdaptiveVertexFitter'),
        chi2cutoff = cms.double(2.5),
        label = cms.string(''),
        maxDistanceToBeam = cms.double(1.0),
        minNdof = cms.double(0.0),
        useBeamConstraint = cms.bool(False)
    ))
)


process.generalTracks = cms.EDProducer("DuplicateListMerger",
    candidateComponents = cms.InputTag("duplicateTrackCandidates","candidateMap"),
    candidateSource = cms.InputTag("duplicateTrackCandidates","candidates"),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    diffHitsCut = cms.int32(5),
    mergedMVAVals = cms.InputTag("duplicateTrackClassifier","MVAValues"),
    mergedSource = cms.InputTag("mergedDuplicateTracks"),
    originalMVAVals = cms.InputTag("preDuplicateMergingGeneralTracks","MVAValues"),
    originalSource = cms.InputTag("preDuplicateMergingGeneralTracks"),
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder')
)


process.globalCombinedSeeds = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag(cms.InputTag("globalSeedsFromTripletsWithVertices"), cms.InputTag("globalSeedsFromPairsWithVertices"))
)


process.globalMixedSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    ClusterCheckPSet = cms.PSet(
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(400000),
        MaxNumberOfPixelClusters = cms.uint32(40000),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
        doClusterCheck = cms.bool(True)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.InputTag("MixedLayerPairs"),
        maxElement = cms.uint32(1000000)
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
        RegionPSet = cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originHalfLength = cms.double(21.2),
            originRadius = cms.double(0.2),
            precise = cms.bool(True),
            ptMin = cms.double(0.9),
            useMultipleScattering = cms.bool(False)
        )
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        MinOneOverPtError = cms.double(1.0),
        OriginTransverseErrorMultiplier = cms.double(1.0),
        SeedMomentumForBOFF = cms.double(5.0),
        TTRHBuilder = cms.string('WithTrackAngle'),
        forceKinematicWithRegionDirection = cms.bool(False),
        magneticField = cms.string('ParabolicMf'),
        propagator = cms.string('PropagatorWithMaterialParabolicMf')
    )
)


process.globalPixelLessSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    ClusterCheckPSet = cms.PSet(
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(5000),
        MaxNumberOfPixelClusters = cms.uint32(40000),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
        doClusterCheck = cms.bool(True)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.InputTag("pixelLessLayerPairs4PixelLessTracking"),
        maxElement = cms.uint32(100000)
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
        RegionPSet = cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originHalfLength = cms.double(40),
            originRadius = cms.double(0.2),
            precise = cms.bool(True),
            ptMin = cms.double(0.9),
            useMultipleScattering = cms.bool(False)
        )
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        MinOneOverPtError = cms.double(1.0),
        OriginTransverseErrorMultiplier = cms.double(1.0),
        SeedMomentumForBOFF = cms.double(5.0),
        TTRHBuilder = cms.string('WithTrackAngle'),
        forceKinematicWithRegionDirection = cms.bool(False),
        magneticField = cms.string('ParabolicMf'),
        propagator = cms.string('PropagatorWithMaterialParabolicMf')
    )
)


process.globalPixelSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    ClusterCheckPSet = cms.PSet(
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(400000),
        MaxNumberOfPixelClusters = cms.uint32(40000),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
        doClusterCheck = cms.bool(True)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.InputTag("PixelLayerPairs")
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
        RegionPSet = cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originHalfLength = cms.double(21.2),
            originRadius = cms.double(0.2),
            precise = cms.bool(True),
            ptMin = cms.double(0.9),
            useMultipleScattering = cms.bool(False)
        )
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        MinOneOverPtError = cms.double(1.0),
        OriginTransverseErrorMultiplier = cms.double(1.0),
        SeedMomentumForBOFF = cms.double(5.0),
        TTRHBuilder = cms.string('WithTrackAngle'),
        forceKinematicWithRegionDirection = cms.bool(False),
        magneticField = cms.string('ParabolicMf'),
        propagator = cms.string('PropagatorWithMaterialParabolicMf')
    )
)


process.globalSeedsFromPairsWithVertices = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    ClusterCheckPSet = cms.PSet(
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(400000),
        MaxNumberOfPixelClusters = cms.uint32(40000),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
        doClusterCheck = cms.bool(True)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitPairGenerator'),
        SeedingLayers = cms.InputTag("MixedLayerPairs"),
        maxElement = cms.uint32(1000000)
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalTrackingRegionWithVerticesProducer'),
        RegionPSet = cms.PSet(
            VertexCollection = cms.InputTag("firstStepPrimaryVertices"),
            beamSpot = cms.InputTag("offlineBeamSpot"),
            fixedError = cms.double(0.2),
            halfLengthScaling4BigEvts = cms.bool(False),
            maxNVertices = cms.int32(-1),
            maxPtMin = cms.double(1000),
            minHalfLength = cms.double(0),
            minOriginR = cms.double(0),
            nSigmaZ = cms.double(4),
            originRScaling4BigEvts = cms.bool(False),
            originRadius = cms.double(0.2),
            pixelClustersForScaling = cms.InputTag("siPixelClusters"),
            precise = cms.bool(True),
            ptMin = cms.double(0.9),
            ptMinScaling4BigEvts = cms.bool(False),
            scalingEndNPix = cms.double(1),
            scalingStartNPix = cms.double(0),
            sigmaZVertex = cms.double(3),
            useFakeVertices = cms.bool(False),
            useFixedError = cms.bool(True),
            useFoundVertices = cms.bool(True),
            useMultipleScattering = cms.bool(False)
        )
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        MinOneOverPtError = cms.double(1.0),
        OriginTransverseErrorMultiplier = cms.double(1.0),
        SeedMomentumForBOFF = cms.double(5.0),
        TTRHBuilder = cms.string('WithTrackAngle'),
        forceKinematicWithRegionDirection = cms.bool(False),
        magneticField = cms.string('ParabolicMf'),
        propagator = cms.string('PropagatorWithMaterialParabolicMf')
    )
)


process.globalSeedsFromTriplets = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    ClusterCheckPSet = cms.PSet(
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(400000),
        MaxNumberOfPixelClusters = cms.uint32(40000),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
        doClusterCheck = cms.bool(True)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('StandardHitTripletGenerator'),
        GeneratorPSet = cms.PSet(
            ComponentName = cms.string('PixelTripletHLTGenerator'),
            SeedComparitorPSet = cms.PSet(
                ComponentName = cms.string('none')
            ),
            extraHitRPhitolerance = cms.double(0.032),
            extraHitRZtolerance = cms.double(0.037),
            maxElement = cms.uint32(1000000),
            phiPreFiltering = cms.double(0.3),
            useBending = cms.bool(True),
            useFixedPreFiltering = cms.bool(False),
            useMultScattering = cms.bool(True)
        ),
        SeedingLayers = cms.InputTag("PixelLayerTriplets")
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
        RegionPSet = cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originHalfLength = cms.double(21.2),
            originRadius = cms.double(0.2),
            precise = cms.bool(True),
            ptMin = cms.double(0.9),
            useMultipleScattering = cms.bool(False)
        )
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        MinOneOverPtError = cms.double(1.0),
        OriginTransverseErrorMultiplier = cms.double(1.0),
        SeedMomentumForBOFF = cms.double(5.0),
        TTRHBuilder = cms.string('WithTrackAngle'),
        forceKinematicWithRegionDirection = cms.bool(False),
        magneticField = cms.string('ParabolicMf'),
        propagator = cms.string('PropagatorWithMaterialParabolicMf')
    )
)


process.globalTrackingRegionWithVertices = cms.EDProducer("GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet(
        VertexCollection = cms.InputTag("firstStepPrimaryVertices"),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        fixedError = cms.double(0.2),
        halfLengthScaling4BigEvts = cms.bool(False),
        maxNVertices = cms.int32(-1),
        maxPtMin = cms.double(1000),
        minHalfLength = cms.double(0),
        minOriginR = cms.double(0),
        nSigmaZ = cms.double(4),
        originRScaling4BigEvts = cms.bool(False),
        originRadius = cms.double(0.2),
        pixelClustersForScaling = cms.InputTag("siPixelClusters"),
        precise = cms.bool(True),
        ptMin = cms.double(0.9),
        ptMinScaling4BigEvts = cms.bool(False),
        scalingEndNPix = cms.double(1),
        scalingStartNPix = cms.double(0),
        sigmaZVertex = cms.double(3),
        useFakeVertices = cms.bool(False),
        useFixedError = cms.bool(True),
        useFoundVertices = cms.bool(True),
        useMultipleScattering = cms.bool(False)
    )
)


process.highPtTripletStep = cms.EDProducer("TrackMVAClassifierPrompt",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorHighPtTripletStep_Phase1')
    ),
    qualityCuts = cms.vdouble(0.2, 0.3, 0.4),
    src = cms.InputTag("highPtTripletStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.highPtTripletStepClusters = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag(""),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trackClassifier = cms.InputTag("","QualityMasks"),
    trajectories = cms.InputTag("")
)


process.highPtTripletStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0, 1),
    maxElement = cms.uint32(50000000),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("highPtTripletStepSeedLayers"),
    trackingRegions = cms.InputTag("highPtTripletStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.highPtTripletStepHitTriplets = cms.EDProducer("CAHitTripletEDProducer",
    CAHardPtCut = cms.double(0.3),
    CAPhiCut = cms.double(0.07),
    CAThetaCut = cms.double(0.004),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("highPtTripletStepHitDoublets"),
    extraHitRPhitolerance = cms.double(0.032),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.8),
        pt2 = cms.double(8),
        value1 = cms.double(100),
        value2 = cms.double(6)
    ),
    useBendingCorrection = cms.bool(True)
)


process.highPtTripletStepMasks = cms.EDProducer("FastTrackerRecHitMaskProducer",
    TrackQuality = cms.string('highPurity'),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    minNumberOfLayersWithMeasBeforeFiltering_ = cms.int32(0),
    oldHitRemovalInfo = cms.InputTag(""),
    recHits = cms.InputTag("fastTrackerRecHits"),
    trackClassifier = cms.InputTag("","QualityMasks"),
    trackQuality = cms.string('hightPurity'),
    trajectories = cms.InputTag("")
)


process.highPtTripletStepSeedClusterMask = cms.EDProducer("SeedClusterRemover",
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trajectories = cms.InputTag("highPtTripletStepSeeds")
)


process.highPtTripletStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("highPtTripletStepClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("highPtTripletStepClusters")
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2+BPix3', 
        'BPix2+BPix3+BPix4', 
        'BPix1+BPix3+BPix4', 
        'BPix1+BPix2+BPix4', 
        'BPix2+BPix3+FPix1_pos', 
        'BPix2+BPix3+FPix1_neg', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+BPix3+FPix1_pos', 
        'BPix1+BPix3+FPix1_neg', 
        'BPix2+FPix1_pos+FPix2_pos', 
        'BPix2+FPix1_neg+FPix2_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg', 
        'BPix1+BPix2+FPix2_pos', 
        'BPix1+BPix2+FPix2_neg', 
        'FPix1_pos+FPix2_pos+FPix3_pos', 
        'FPix1_neg+FPix2_neg+FPix3_neg', 
        'BPix1+FPix2_pos+FPix3_pos', 
        'BPix1+FPix2_neg+FPix3_neg', 
        'BPix1+FPix1_pos+FPix3_pos', 
        'BPix1+FPix1_neg+FPix3_neg'
    )
)


process.highPtTripletStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("highPtTripletStepHitTriplets")
)


process.highPtTripletStepSelector = cms.EDProducer("MultiTrackSelector",
    beamspot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("highPtTripletStepTracks"),
    trackSelectors = cms.VPSet(
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(2.0),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.7, 4.0),
            d0_par2 = cms.vdouble(0.6, 4.0),
            dz_par1 = cms.vdouble(0.8, 4.0),
            dz_par2 = cms.vdouble(0.6, 4.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(3),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('highPtTripletStepLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.002),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(1.0),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.6, 4.0),
            d0_par2 = cms.vdouble(0.5, 4.0),
            dz_par1 = cms.vdouble(0.7, 4.0),
            dz_par2 = cms.vdouble(0.6, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('highPtTripletStepTight'),
            preFilterName = cms.string('highPtTripletStepLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.002),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.8),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.6, 4.0),
            d0_par2 = cms.vdouble(0.45, 4.0),
            dz_par1 = cms.vdouble(0.7, 4.0),
            dz_par2 = cms.vdouble(0.55, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(4),
            minNumberLayers = cms.uint32(4),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(4),
            nSigmaZ = cms.double(4.0),
            name = cms.string('highPtTripletStep'),
            preFilterName = cms.string('highPtTripletStepTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        )
    ),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.highPtTripletStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('highPtTripletStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("highPtTripletStepClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("highPtTripletStepSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.highPtTripletStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(4),
        originHalfLength = cms.double(0),
        originRadius = cms.double(0.02),
        precise = cms.bool(True),
        ptMin = cms.double(0.55),
        useMultipleScattering = cms.bool(False)
    )
)


process.highPtTripletStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('highPtTripletStep'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("highPtTripletStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.initialStep = cms.EDProducer("ClassifierMerger",
    inputClassifiers = cms.vstring(
        'initialStepClassifier1', 
        'initialStepClassifier2', 
        'initialStepClassifier3'
    )
)


process.initialStepClassifier1 = cms.EDProducer("TrackMVAClassifierPrompt",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorIter0_13TeV')
    ),
    qualityCuts = cms.vdouble(-0.9, -0.8, -0.7),
    src = cms.InputTag("initialStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.initialStepClassifier2 = cms.EDProducer("TrackMVAClassifierDetached",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorIter3_13TeV')
    ),
    qualityCuts = cms.vdouble(-0.5, 0.0, 0.5),
    src = cms.InputTag("initialStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.initialStepClassifier3 = cms.EDProducer("TrackMVAClassifierPrompt",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorIter1_13TeV')
    ),
    qualityCuts = cms.vdouble(-0.6, -0.3, -0.1),
    src = cms.InputTag("initialStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.initialStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(50000000),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("initialStepSeedLayers"),
    trackingRegions = cms.InputTag("initialStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.initialStepHitDoubletsPreSplitting = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheckPreSplitting"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(50000000),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("initialStepSeedLayersPreSplitting"),
    trackingRegions = cms.InputTag("initialStepTrackingRegionsPreSplitting"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.initialStepHitQuadruplets = cms.EDProducer("CAHitQuadrupletEDProducer",
    CAHardPtCut = cms.double(0),
    CAPhiCut = cms.double(0.2),
    CAThetaCut = cms.double(0.0012),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("initialStepHitDoublets"),
    extraHitRPhitolerance = cms.double(0.032),
    fitFastCircle = cms.bool(True),
    fitFastCircleChi2Cut = cms.bool(True),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.7),
        pt2 = cms.double(2),
        value1 = cms.double(200),
        value2 = cms.double(50)
    ),
    useBendingCorrection = cms.bool(True)
)


process.initialStepHitQuadrupletsPreSplitting = cms.EDProducer("CAHitQuadrupletEDProducer",
    CAHardPtCut = cms.double(0),
    CAPhiCut = cms.double(0.2),
    CAThetaCut = cms.double(0.0012),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCachePreSplitting"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("initialStepHitDoubletsPreSplitting"),
    extraHitRPhitolerance = cms.double(0.032),
    fitFastCircle = cms.bool(True),
    fitFastCircleChi2Cut = cms.bool(True),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.7),
        pt2 = cms.double(2),
        value1 = cms.double(200),
        value2 = cms.double(50)
    ),
    useBendingCorrection = cms.bool(True)
)


process.initialStepHitTriplets = cms.EDProducer("PixelTripletHLTEDProducer",
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("initialStepHitDoublets"),
    extraHitRPhitolerance = cms.double(0.032),
    extraHitRZtolerance = cms.double(0.037),
    maxElement = cms.uint32(1000000),
    phiPreFiltering = cms.double(0.3),
    produceIntermediateHitTriplets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    useBending = cms.bool(True),
    useFixedPreFiltering = cms.bool(False),
    useMultScattering = cms.bool(True)
)


process.initialStepHitTripletsPreSplitting = cms.EDProducer("PixelTripletHLTEDProducer",
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCachePreSplitting"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("initialStepHitDoubletsPreSplitting"),
    extraHitRPhitolerance = cms.double(0.032),
    extraHitRZtolerance = cms.double(0.037),
    maxElement = cms.uint32(1000000),
    phiPreFiltering = cms.double(0.3),
    produceIntermediateHitTriplets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    useBending = cms.bool(True),
    useFixedPreFiltering = cms.bool(False),
    useMultScattering = cms.bool(True)
)


process.initialStepSeedClusterMask = cms.EDProducer("SeedClusterRemover",
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trajectories = cms.InputTag("initialStepSeeds")
)


process.initialStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'
    )
)


process.initialStepSeedLayersPreSplitting = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHitsPreSplitting'),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHitsPreSplitting'),
        TTRHBuilder = cms.string('WithTrackAngle')
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'
    )
)


process.initialStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("initialStepHitTriplets")
)


process.initialStepSeedsPreSplitting = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("initialStepHitTripletsPreSplitting")
)


process.initialStepSelector = cms.EDProducer("MultiTrackSelector",
    GBRForestLabel = cms.string('MVASelectorIter0'),
    beamspot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("initialStepTracks"),
    trackSelectors = cms.VPSet(
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(1.6),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.55, 4.0),
            d0_par2 = cms.vdouble(0.55, 4.0),
            dz_par1 = cms.vdouble(0.65, 4.0),
            dz_par2 = cms.vdouble(0.45, 4.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(999),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(0),
            minNumberLayers = cms.uint32(0),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('initialStepLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.01),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.7),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.3, 4.0),
            d0_par2 = cms.vdouble(0.4, 4.0),
            dz_par1 = cms.vdouble(0.35, 4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('initialStepTight'),
            preFilterName = cms.string('initialStepLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.01),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.7),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.3, 4.0),
            d0_par2 = cms.vdouble(0.4, 4.0),
            dz_par1 = cms.vdouble(0.35, 4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('QualityMasks'),
            preFilterName = cms.string('initialStepTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        )
    ),
    useAnyMVA = cms.bool(False),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.initialStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('initialStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("initialStepSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.initialStepTrackCandidatesPreSplitting = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEventPreSplitting"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('initialStepTrajectoryBuilderPreSplitting')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("initialStepSeedsPreSplitting"),
    useHitsSplitting = cms.bool(True)
)


process.initialStepTrackRefsForJets = cms.EDProducer("ChargedRefCandidateProducer",
    particleType = cms.string('pi+'),
    src = cms.InputTag("initialStepTracks")
)


process.initialStepTrackRefsForJetsPreSplitting = cms.EDProducer("ChargedRefCandidateProducer",
    particleType = cms.string('pi+'),
    src = cms.InputTag("initialStepTracksPreSplitting")
)


process.initialStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(4),
        originHalfLength = cms.double(0),
        originRadius = cms.double(0.02),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        useMultipleScattering = cms.bool(False)
    )
)


process.initialStepTrackingRegionsPreSplitting = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(4),
        originHalfLength = cms.double(0),
        originRadius = cms.double(0.02),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        useMultipleScattering = cms.bool(False)
    )
)


process.initialStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('initialStep'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("initialStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.initialStepTracksPreSplitting = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('initialStep'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEventPreSplitting"),
    NavigationSchool = cms.string(''),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("initialStepTrackCandidatesPreSplitting"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.jetCoreClusterSplitter = cms.EDProducer("JetCoreClusterSplitter",
    centralMIPCharge = cms.double(26000),
    chargeFractionMin = cms.double(2.0),
    chargePerUnit = cms.double(2000),
    cores = cms.InputTag("ak5CaloJets"),
    deltaRmax = cms.double(0.05),
    forceXError = cms.double(100),
    forceYError = cms.double(150),
    fractionalWidth = cms.double(0.4),
    pixelCPE = cms.string('PixelCPEGeneric'),
    pixelClusters = cms.InputTag("siPixelCluster"),
    ptMin = cms.double(200),
    verbose = cms.bool(False),
    vertices = cms.InputTag("offlinePrimaryVertices")
)


process.jetCoreRegionalStep = cms.EDProducer("TrackCutClassifier",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            drWPVerr_par = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dr_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dr_par1 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dr_par2 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38)
        ),
        dz_par = cms.PSet(
            dzWPVerr_par = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dz_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dz_par1 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dz_par2 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38)
        ),
        isHLT = cms.bool(False),
        maxChi2 = cms.vdouble(9999.0, 9999.0, 9999.0),
        maxChi2n = cms.vdouble(1.6, 1.0, 0.7),
        maxDr = cms.vdouble(0.3, 0.2, 0.1),
        maxDz = cms.vdouble(0.5, 0.35, 0.2),
        maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24, 15),
        maxLostLayers = cms.vint32(4, 3, 2),
        maxRelPtErr = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        min3DLayers = cms.vint32(1, 2, 3),
        minHits = cms.vint32(0, 0, 1),
        minHits4pass = cms.vint32(2147483647, 2147483647, 2147483647),
        minLayers = cms.vint32(3, 5, 5),
        minNVtxTrk = cms.int32(2),
        minNdof = cms.vdouble(-1, -1, -1),
        minPixelHits = cms.vint32(1, 1, 1)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("jetCoreRegionalStepTracks"),
    vertices = cms.InputTag("firstStepGoodPrimaryVertices")
)


process.jetCoreRegionalStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(1000000),
    maxElementTotal = cms.uint32(12000000),
    produceIntermediateHitDoublets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    seedingLayers = cms.InputTag("jetCoreRegionalStepSeedLayers"),
    trackingRegions = cms.InputTag("jetCoreRegionalStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.jetCoreRegionalStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        useErrorsFromParam = cms.bool(True)
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        useErrorsFromParam = cms.bool(True)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit")
    ),
    layerList = cms.vstring(
        'BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg', 
        'BPix3+TIB1', 
        'BPix3+TIB2'
    )
)


process.jetCoreRegionalStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(True),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("jetCoreRegionalStepHitDoublets")
)


process.jetCoreRegionalStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('jetCoreRegionalStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(10000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("jetCoreRegionalStepSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.jetCoreRegionalStepTrackingRegions = cms.EDProducer("TauRegionalPixelSeedTrackingRegionEDProducer",
    RegionPSet = cms.PSet(
        JetSrc = cms.InputTag("jetsForCoreTracking"),
        deltaEtaRegion = cms.double(0.2),
        deltaPhiRegion = cms.double(0.2),
        howToUseMeasurementTracker = cms.string('Never'),
        measurementTrackerName = cms.InputTag("MeasurementTrackerEvent"),
        originHalfLength = cms.double(0.2),
        originRadius = cms.double(0.2),
        ptMin = cms.double(10),
        searchOpt = cms.bool(False),
        vertexSrc = cms.InputTag("firstStepGoodPrimaryVertices")
    )
)


process.jetCoreRegionalStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('jetCoreRegionalStep'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("jetCoreRegionalStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.lowPtQuadStep = cms.EDProducer("TrackMVAClassifierPrompt",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorLowPtQuadStep_Phase1')
    ),
    qualityCuts = cms.vdouble(-0.7, -0.35, -0.15),
    src = cms.InputTag("lowPtQuadStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.lowPtQuadStepClusters = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag(""),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trackClassifier = cms.InputTag("","QualityMasks"),
    trajectories = cms.InputTag("")
)


process.lowPtQuadStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0, 1, 2),
    maxElement = cms.uint32(50000000),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("lowPtQuadStepSeedLayers"),
    trackingRegions = cms.InputTag("lowPtQuadStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.lowPtQuadStepHitQuadruplets = cms.EDProducer("CAHitQuadrupletEDProducer",
    CAHardPtCut = cms.double(0),
    CAPhiCut = cms.double(0.3),
    CAThetaCut = cms.double(0.0017),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("lowPtQuadStepHitDoublets"),
    extraHitRPhitolerance = cms.double(0.032),
    fitFastCircle = cms.bool(True),
    fitFastCircleChi2Cut = cms.bool(True),
    maxChi2 = cms.PSet(
        enabled = cms.bool(True),
        pt1 = cms.double(0.7),
        pt2 = cms.double(2),
        value1 = cms.double(1000),
        value2 = cms.double(150)
    ),
    useBendingCorrection = cms.bool(True)
)


process.lowPtQuadStepMasks = cms.EDProducer("FastTrackerRecHitMaskProducer",
    TrackQuality = cms.string('highPurity'),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    minNumberOfLayersWithMeasBeforeFiltering_ = cms.int32(0),
    oldHitRemovalInfo = cms.InputTag(""),
    recHits = cms.InputTag("fastTrackerRecHits"),
    trackClassifier = cms.InputTag("","QualityMasks"),
    trackQuality = cms.string('hightPurity'),
    trajectories = cms.InputTag("")
)


process.lowPtQuadStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtQuadStepClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtQuadStepClusters")
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2+BPix3+BPix4', 
        'BPix1+BPix2+BPix3+FPix1_pos', 
        'BPix1+BPix2+BPix3+FPix1_neg', 
        'BPix1+BPix2+FPix1_pos+FPix2_pos', 
        'BPix1+BPix2+FPix1_neg+FPix2_neg', 
        'BPix1+FPix1_pos+FPix2_pos+FPix3_pos', 
        'BPix1+FPix1_neg+FPix2_neg+FPix3_neg'
    )
)


process.lowPtQuadStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("lowPtQuadStepHitQuadruplets")
)


process.lowPtQuadStepSelector = cms.EDProducer("MultiTrackSelector",
    beamspot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("lowPtQuadStepTracks"),
    trackSelectors = cms.VPSet(
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(2.0),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.8, 4.0),
            d0_par2 = cms.vdouble(0.6, 4.0),
            dz_par1 = cms.vdouble(0.7, 4.0),
            dz_par2 = cms.vdouble(0.6, 4.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('lowPtQuadStepLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.002),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(1.4),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.7, 4.0),
            d0_par2 = cms.vdouble(0.5, 4.0),
            dz_par1 = cms.vdouble(0.6, 4.0),
            dz_par2 = cms.vdouble(0.5, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('lowPtQuadStepTight'),
            preFilterName = cms.string('lowPtQuadStepLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.002),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(1.2),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.5, 4.0),
            d0_par2 = cms.vdouble(0.45, 4.0),
            dz_par1 = cms.vdouble(0.5, 4.0),
            dz_par2 = cms.vdouble(0.45, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('lowPtQuadStep'),
            preFilterName = cms.string('lowPtQuadStepTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        )
    ),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.lowPtQuadStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('lowPtQuadStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('lowPtQuadStepTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("lowPtQuadStepClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("lowPtQuadStepSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.lowPtQuadStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(4),
        originHalfLength = cms.double(0),
        originRadius = cms.double(0.02),
        precise = cms.bool(True),
        ptMin = cms.double(0.15),
        useMultipleScattering = cms.bool(False)
    )
)


process.lowPtQuadStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('lowPtQuadStep'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("lowPtQuadStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.lowPtTripletStep = cms.EDProducer("TrackMVAClassifierPrompt",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorIter1_13TeV')
    ),
    qualityCuts = cms.vdouble(-0.6, -0.3, -0.1),
    src = cms.InputTag("lowPtTripletStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.lowPtTripletStepClusters = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag("detachedTripletStepClusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trackClassifier = cms.InputTag("detachedTripletStep","QualityMasks"),
    trajectories = cms.InputTag("detachedTripletStepTracks")
)


process.lowPtTripletStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(50000000),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("lowPtTripletStepSeedLayers"),
    trackingRegions = cms.InputTag("lowPtTripletStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.lowPtTripletStepHitTriplets = cms.EDProducer("PixelTripletHLTEDProducer",
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('LowPtClusterShapeSeedComparitor'),
        clusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        clusterShapeHitFilter = cms.string('ClusterShapeHitFilter')
    ),
    doublets = cms.InputTag("lowPtTripletStepHitDoublets"),
    extraHitRPhitolerance = cms.double(0.032),
    extraHitRZtolerance = cms.double(0.037),
    maxElement = cms.uint32(1000000),
    phiPreFiltering = cms.double(0.3),
    produceIntermediateHitTriplets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    useBending = cms.bool(True),
    useFixedPreFiltering = cms.bool(False),
    useMultScattering = cms.bool(True)
)


process.lowPtTripletStepMasks = cms.EDProducer("FastTrackerRecHitMaskProducer",
    TrackQuality = cms.string('highPurity'),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    minNumberOfLayersWithMeasBeforeFiltering_ = cms.int32(0),
    oldHitRemovalInfo = cms.InputTag("detachedTripletStepMasks"),
    recHits = cms.InputTag("fastTrackerRecHits"),
    trackClassifier = cms.InputTag("detachedTripletStep","QualityMasks"),
    trackQuality = cms.string('hightPurity'),
    trajectories = cms.InputTag("detachedTripletStepTracks")
)


process.lowPtTripletStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtTripletStepClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("lowPtTripletStepClusters")
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'
    )
)


process.lowPtTripletStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("lowPtTripletStepHitTriplets")
)


process.lowPtTripletStepSelector = cms.EDProducer("MultiTrackSelector",
    GBRForestLabel = cms.string('MVASelectorIter1'),
    beamspot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("lowPtTripletStepTracks"),
    trackSelectors = cms.VPSet(
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(1.6),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.55, 4.0),
            d0_par2 = cms.vdouble(0.55, 4.0),
            dz_par1 = cms.vdouble(0.65, 4.0),
            dz_par2 = cms.vdouble(0.45, 4.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(999),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(0),
            minNumberLayers = cms.uint32(0),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('lowPtTripletStepLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.01),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.7),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.3, 4.0),
            d0_par2 = cms.vdouble(0.4, 4.0),
            dz_par1 = cms.vdouble(0.35, 4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('lowPtTripletStepTight'),
            preFilterName = cms.string('lowPtTripletStepLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.01),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.7),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.3, 4.0),
            d0_par2 = cms.vdouble(0.4, 4.0),
            dz_par1 = cms.vdouble(0.35, 4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('QualityMasks'),
            preFilterName = cms.string('lowPtTripletStepTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        )
    ),
    useAnyMVA = cms.bool(False),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.lowPtTripletStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('lowPtTripletStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('lowPtTripletStepTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("lowPtTripletStepClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("lowPtTripletStepSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.lowPtTripletStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(4),
        originHalfLength = cms.double(0),
        originRadius = cms.double(0.02),
        precise = cms.bool(True),
        ptMin = cms.double(0.2),
        useMultipleScattering = cms.bool(False)
    )
)


process.lowPtTripletStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('lowPtTripletStep'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("lowPtTripletStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.mergedDuplicateTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('undefAlgorithm'),
    Fitter = cms.string('RKFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("duplicateTrackCandidates","candidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.mixedTripletStep = cms.EDProducer("ClassifierMerger",
    inputClassifiers = cms.vstring(
        'mixedTripletStepClassifier1', 
        'mixedTripletStepClassifier2'
    )
)


process.mixedTripletStepClassifier1 = cms.EDProducer("TrackMVAClassifierDetached",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorIter4_13TeV')
    ),
    qualityCuts = cms.vdouble(-0.5, 0.0, 0.5),
    src = cms.InputTag("mixedTripletStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.mixedTripletStepClassifier2 = cms.EDProducer("TrackMVAClassifierPrompt",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorIter0_13TeV')
    ),
    qualityCuts = cms.vdouble(-0.2, -0.2, -0.2),
    src = cms.InputTag("mixedTripletStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.mixedTripletStepClusters = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag("chargeCut2069Clusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trackClassifier = cms.InputTag("pixelPairStep","QualityMasks"),
    trajectories = cms.InputTag("pixelPairStepTracks")
)


process.mixedTripletStepHitDoubletsA = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(50000000),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("mixedTripletStepSeedLayersA"),
    trackingRegions = cms.InputTag("mixedTripletStepTrackingRegionsA"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.mixedTripletStepHitDoubletsB = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(50000000),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("mixedTripletStepSeedLayersB"),
    trackingRegions = cms.InputTag("mixedTripletStepTrackingRegionsB"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.mixedTripletStepHitTripletsA = cms.EDProducer("PixelTripletLargeTipEDProducer",
    doublets = cms.InputTag("mixedTripletStepHitDoubletsA"),
    extraHitRPhitolerance = cms.double(0),
    extraHitRZtolerance = cms.double(0),
    maxElement = cms.uint32(1000000),
    phiPreFiltering = cms.double(0.3),
    produceIntermediateHitTriplets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    useBending = cms.bool(True),
    useFixedPreFiltering = cms.bool(False),
    useMultScattering = cms.bool(True)
)


process.mixedTripletStepHitTripletsB = cms.EDProducer("PixelTripletLargeTipEDProducer",
    doublets = cms.InputTag("mixedTripletStepHitDoubletsB"),
    extraHitRPhitolerance = cms.double(0),
    extraHitRZtolerance = cms.double(0),
    maxElement = cms.uint32(1000000),
    phiPreFiltering = cms.double(0.3),
    produceIntermediateHitTriplets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    useBending = cms.bool(True),
    useFixedPreFiltering = cms.bool(False),
    useMultScattering = cms.bool(True)
)


process.mixedTripletStepMasks = cms.EDProducer("FastTrackerRecHitMaskProducer",
    TrackQuality = cms.string('highPurity'),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    minNumberOfLayersWithMeasBeforeFiltering_ = cms.int32(0),
    oldHitRemovalInfo = cms.InputTag("pixelPairStepMasks"),
    recHits = cms.InputTag("fastTrackerRecHits"),
    trackClassifier = cms.InputTag("pixelPairStep","QualityMasks"),
    trackQuality = cms.string('hightPurity'),
    trajectories = cms.InputTag("pixelPairStepTracks")
)


process.mixedTripletStepSeedClusterMask = cms.EDProducer("SeedClusterRemover",
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    oldClusterRemovalInfo = cms.InputTag("pixelPairStepSeedClusterMask"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trajectories = cms.InputTag("mixedTripletStepSeeds")
)


process.mixedTripletStepSeedLayersA = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters")
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(1),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("mixedTripletStepClusters"),
        useRingSlector = cms.bool(True)
    ),
    layerList = cms.vstring(
        'BPix2+FPix1_pos+FPix2_pos', 
        'BPix2+FPix1_neg+FPix2_neg'
    )
)


process.mixedTripletStepSeedLayersB = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("mixedTripletStepClusters")
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        skipClusters = cms.InputTag("mixedTripletStepClusters")
    ),
    layerList = cms.vstring('BPix2+BPix3+TIB1')
)


process.mixedTripletStepSeeds = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag(cms.InputTag("mixedTripletStepSeedsA"), cms.InputTag("mixedTripletStepSeedsB"))
)


process.mixedTripletStepSeedsA = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        ClusterShapeHitFilterName = cms.string('mixedTripletStepClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(True)
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsA")
)


process.mixedTripletStepSeedsB = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        ClusterShapeHitFilterName = cms.string('mixedTripletStepClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(False),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(True)
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("mixedTripletStepHitTripletsB")
)


process.mixedTripletStepSelector = cms.EDProducer("MultiTrackSelector",
    GBRForestLabel = cms.string('MVASelectorIter4'),
    beamspot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("mixedTripletStepTracks"),
    trackSelectors = cms.VPSet(
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(1.2),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(1.2, 3.0),
            d0_par2 = cms.vdouble(1.3, 3.0),
            dz_par1 = cms.vdouble(1.2, 3.0),
            dz_par2 = cms.vdouble(1.3, 3.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(2),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('mixedTripletStepVtxLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.6),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(1.2, 4.0),
            d0_par2 = cms.vdouble(1.2, 4.0),
            dz_par1 = cms.vdouble(1.2, 4.0),
            dz_par2 = cms.vdouble(1.2, 4.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(4),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('mixedTripletStepTrkLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.6),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(1.1, 3.0),
            d0_par2 = cms.vdouble(1.2, 3.0),
            dz_par1 = cms.vdouble(1.1, 3.0),
            dz_par2 = cms.vdouble(1.2, 3.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('mixedTripletStepVtxTight'),
            preFilterName = cms.string('mixedTripletStepVtxLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.4),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(1.1, 4.0),
            d0_par2 = cms.vdouble(1.1, 4.0),
            dz_par1 = cms.vdouble(1.1, 4.0),
            dz_par2 = cms.vdouble(1.1, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(4),
            minNumberLayers = cms.uint32(5),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('mixedTripletStepTrkTight'),
            preFilterName = cms.string('mixedTripletStepTrkLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.4),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(1.1, 3.0),
            d0_par2 = cms.vdouble(1.2, 3.0),
            dz_par1 = cms.vdouble(1.1, 3.0),
            dz_par2 = cms.vdouble(1.2, 3.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('mixedTripletStepVtx'),
            preFilterName = cms.string('mixedTripletStepVtxTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.3),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.9, 4.0),
            d0_par2 = cms.vdouble(0.9, 4.0),
            dz_par1 = cms.vdouble(0.9, 4.0),
            dz_par2 = cms.vdouble(0.9, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(0),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(4),
            minNumberLayers = cms.uint32(5),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('mixedTripletStepTrk'),
            preFilterName = cms.string('mixedTripletStepTrkTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        )
    ),
    useAnyMVA = cms.bool(False),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.mixedTripletStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('mixedTripletStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('mixedTripletStepTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("mixedTripletStepClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("mixedTripletStepSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.mixedTripletStepTrackingRegionsA = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(0),
        originHalfLength = cms.double(15.0),
        originRadius = cms.double(1.5),
        precise = cms.bool(True),
        ptMin = cms.double(0.4),
        useMultipleScattering = cms.bool(False)
    )
)


process.mixedTripletStepTrackingRegionsB = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(0),
        originHalfLength = cms.double(10.0),
        originRadius = cms.double(1.5),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        useMultipleScattering = cms.bool(False)
    )
)


process.mixedTripletStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('mixedTripletStep'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("mixedTripletStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.muonSeededSeedsInOut = cms.EDProducer("MuonReSeeder",
    DoPredictionsOnly = cms.bool(False),
    Fitter = cms.string('KFFitterForRefitInsideOut'),
    MTDRecHitBuilder = cms.string('MTDRecHitBuilder'),
    MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
    Propagator = cms.string('SmartPropagatorAnyRKOpposite'),
    RefitDirection = cms.string('alongMomentum'),
    RefitRPCHits = cms.bool(True),
    Smoother = cms.string('KFSmootherForRefitInsideOut'),
    TrackerRecHitBuilder = cms.string('WithAngleAndTemplate'),
    cut = cms.string('pt > 2'),
    debug = cms.untracked.bool(False),
    insideOut = cms.bool(True),
    layersToKeep = cms.int32(5),
    src = cms.InputTag("earlyMuons")
)


process.muonSeededSeedsInOutAsTracks = cms.EDProducer("FakeTrackProducerFromSeed",
    src = cms.InputTag("muonSeededSeedsInOut")
)


process.muonSeededSeedsOutIn = cms.EDProducer("OutsideInMuonSeeder",
    cut = cms.string('pt > 10 && outerTrack.hitPattern.muonStationsWithValidHits >= 2'),
    debug = cms.untracked.bool(False),
    errorRescaleFactor = cms.double(2.0),
    fromVertex = cms.bool(True),
    hitCollector = cms.string('hitCollectorForOutInMuonSeeds'),
    hitsToTry = cms.int32(3),
    layersToTry = cms.int32(3),
    maxEtaForTOB = cms.double(1.8),
    minEtaForTEC = cms.double(0.7),
    muonPropagator = cms.string('SteppingHelixPropagatorAlong'),
    src = cms.InputTag("earlyMuons"),
    trackerPropagator = cms.string('PropagatorWithMaterial')
)


process.muonSeededSeedsOutInAsTracks = cms.EDProducer("FakeTrackProducerFromSeed",
    src = cms.InputTag("muonSeededSeedsOutIn")
)


process.muonSeededTrackCandidatesInOut = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('none'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('muonSeededTrajectoryBuilderForInOut')
    ),
    TrajectoryCleaner = cms.string('muonSeededTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("muonSeededSeedsInOut"),
    useHitsSplitting = cms.bool(True)
)


process.muonSeededTrackCandidatesInOutAsTracks = cms.EDProducer("FakeTrackProducerFromCandidate",
    src = cms.InputTag("muonSeededTrackCandidatesInOut")
)


process.muonSeededTrackCandidatesOutIn = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('muonSeededTrajectoryBuilderForOutIn')
    ),
    TrajectoryCleaner = cms.string('muonSeededTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(False),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("muonSeededSeedsOutIn"),
    useHitsSplitting = cms.bool(True)
)


process.muonSeededTrackCandidatesOutInAsTracks = cms.EDProducer("FakeTrackProducerFromCandidate",
    src = cms.InputTag("muonSeededTrackCandidatesOutIn")
)


process.muonSeededTracksInOut = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('muonSeededStepInOut'),
    Fitter = cms.string('muonSeededFittingSmootherWithOutliersRejectionAndRK'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("muonSeededTrackCandidatesInOut"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.muonSeededTracksInOutClassifier = cms.EDProducer("TrackCutClassifier",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            drWPVerr_par = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dr_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dr_par1 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dr_par2 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38)
        ),
        dz_par = cms.PSet(
            dzWPVerr_par = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dz_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dz_par1 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dz_par2 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38)
        ),
        isHLT = cms.bool(False),
        maxChi2 = cms.vdouble(9999.0, 9999.0, 9999.0),
        maxChi2n = cms.vdouble(10.0, 1.0, 0.4),
        maxDr = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        maxDz = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24, 15),
        maxLostLayers = cms.vint32(4, 3, 2),
        maxRelPtErr = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        min3DLayers = cms.vint32(1, 2, 2),
        minHits = cms.vint32(0, 0, 1),
        minHits4pass = cms.vint32(2147483647, 2147483647, 2147483647),
        minLayers = cms.vint32(3, 5, 5),
        minNVtxTrk = cms.int32(2),
        minNdof = cms.vdouble(-1, -1, -1),
        minPixelHits = cms.vint32(0, 0, 0)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("muonSeededTracksInOut"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.muonSeededTracksInOutSelector = cms.EDProducer("MultiTrackSelector",
    beamspot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("muonSeededTracksInOut"),
    trackSelectors = cms.VPSet(
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(False),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(10.0),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.55, 4.0),
            d0_par2 = cms.vdouble(0.55, 4.0),
            dz_par1 = cms.vdouble(0.65, 4.0),
            dz_par2 = cms.vdouble(0.45, 4.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(4),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(7),
            minNumber3DLayers = cms.uint32(0),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(5),
            nSigmaZ = cms.double(4.0),
            name = cms.string('muonSeededTracksInOutLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.01),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(False),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(1.0),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.3, 4.0),
            d0_par2 = cms.vdouble(0.4, 4.0),
            dz_par1 = cms.vdouble(0.35, 4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(3),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(10),
            minNumber3DLayers = cms.uint32(2),
            minNumberLayers = cms.uint32(5),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(6),
            nSigmaZ = cms.double(4.0),
            name = cms.string('muonSeededTracksInOutTight'),
            preFilterName = cms.string('muonSeededTracksInOutLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.01),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(False),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.4),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.3, 4.0),
            d0_par2 = cms.vdouble(0.4, 4.0),
            dz_par1 = cms.vdouble(0.35, 4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(2),
            minNumberLayers = cms.uint32(5),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(7),
            nSigmaZ = cms.double(4.0),
            name = cms.string('muonSeededTracksInOutHighPurity'),
            preFilterName = cms.string('muonSeededTracksInOutTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        )
    ),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.muonSeededTracksOutIn = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('muonSeededStepOutIn'),
    Fitter = cms.string('muonSeededFittingSmootherWithOutliersRejectionAndRK'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("muonSeededTrackCandidatesOutIn"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.muonSeededTracksOutInClassifier = cms.EDProducer("TrackCutClassifier",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        dr_par = cms.PSet(
            d0err = cms.vdouble(0.003, 0.003, 0.003),
            d0err_par = cms.vdouble(0.001, 0.001, 0.001),
            drWPVerr_par = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dr_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dr_par1 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dr_par2 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38)
        ),
        dz_par = cms.PSet(
            dzWPVerr_par = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dz_exp = cms.vint32(2147483647, 2147483647, 2147483647),
            dz_par1 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
            dz_par2 = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38)
        ),
        isHLT = cms.bool(False),
        maxChi2 = cms.vdouble(9999.0, 9999.0, 9999.0),
        maxChi2n = cms.vdouble(10.0, 1.0, 0.4),
        maxDr = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        maxDz = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        maxDzWrtBS = cms.vdouble(3.40282346639e+38, 24, 15),
        maxLostLayers = cms.vint32(4, 3, 2),
        maxRelPtErr = cms.vdouble(3.40282346639e+38, 3.40282346639e+38, 3.40282346639e+38),
        min3DLayers = cms.vint32(1, 2, 2),
        minHits = cms.vint32(0, 0, 1),
        minHits4pass = cms.vint32(2147483647, 2147483647, 2147483647),
        minLayers = cms.vint32(3, 5, 5),
        minNVtxTrk = cms.int32(2),
        minNdof = cms.vdouble(-1, -1, -1),
        minPixelHits = cms.vint32(0, 0, 0)
    ),
    qualityCuts = cms.vdouble(-0.7, 0.1, 0.7),
    src = cms.InputTag("muonSeededTracksOutIn"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.muonSeededTracksOutInSelector = cms.EDProducer("MultiTrackSelector",
    beamspot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("muonSeededTracksOutIn"),
    trackSelectors = cms.VPSet(
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(False),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(10.0),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.55, 4.0),
            d0_par2 = cms.vdouble(0.55, 4.0),
            dz_par1 = cms.vdouble(0.65, 4.0),
            dz_par2 = cms.vdouble(0.45, 4.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(4),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(7),
            minNumber3DLayers = cms.uint32(0),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(5),
            nSigmaZ = cms.double(4.0),
            name = cms.string('muonSeededTracksOutInLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.01),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(False),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(1.0),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.3, 4.0),
            d0_par2 = cms.vdouble(0.4, 4.0),
            dz_par1 = cms.vdouble(0.35, 4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(3),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(10),
            minNumber3DLayers = cms.uint32(2),
            minNumberLayers = cms.uint32(5),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(6),
            nSigmaZ = cms.double(4.0),
            name = cms.string('muonSeededTracksOutInTight'),
            preFilterName = cms.string('muonSeededTracksOutInLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.01),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(False),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.4),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.3, 4.0),
            d0_par2 = cms.vdouble(0.4, 4.0),
            dz_par1 = cms.vdouble(0.35, 4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(2),
            minNumberLayers = cms.uint32(5),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(7),
            nSigmaZ = cms.double(4.0),
            name = cms.string('muonSeededTracksOutInHighPurity'),
            preFilterName = cms.string('muonSeededTracksOutInTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        )
    ),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.myOfflineBeamSpot = cms.EDProducer("BeamSpotProducer")


process.newCombinedSeeds = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag(
        cms.InputTag("initialStepSeeds"), cms.InputTag("pixelPairStepSeeds"), cms.InputTag("mixedTripletStepSeeds"), cms.InputTag("pixelLessStepSeeds"), cms.InputTag("tripletElectronSeeds"), 
        cms.InputTag("pixelPairElectronSeeds"), cms.InputTag("stripPairElectronSeeds")
    )
)


process.photonConvTrajSeedFromQuadruplets = cms.EDProducer("PhotonConversionTrajectorySeedProducerFromQuadruplets",
    ClusterCheckPSet = cms.PSet(
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(50000),
        MaxNumberOfPixelClusters = cms.uint32(10000),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        doClusterCheck = cms.bool(True)
    ),
    DoxcheckSeedCandidates = cms.bool(False),
    OrderedHitsFactoryPSet = cms.PSet(
        SeedingLayers = cms.InputTag("conv2LayerPairs"),
        maxElement = cms.uint32(900000)
    ),
    QuadCutPSet = cms.PSet(
        Cut_BeamPipeRadius = cms.double(3.0),
        Cut_DeltaRho = cms.double(12.0),
        Cut_maxLegPt = cms.double(10.0),
        Cut_minLegPt = cms.double(0.6),
        Cut_zCA = cms.double(100),
        apply_Arbitration = cms.bool(True),
        apply_ClusterShapeFilter = cms.bool(True),
        apply_DeltaPhiCuts = cms.bool(True),
        apply_zCACut = cms.bool(False),
        rejectAllQuads = cms.bool(False)
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
        RegionPSet = cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originHalfLength = cms.double(12.0),
            originRadius = cms.double(3.0),
            precise = cms.bool(True),
            ptMin = cms.double(0.2)
        )
    ),
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(True),
        FilterPixelHits = cms.bool(False),
        FilterStripHits = cms.bool(True)
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedForPhotonConversionFromQuadruplets'),
        SeedMomentumForBOFF = cms.double(5.0),
        propagator = cms.string('PropagatorWithMaterial')
    ),
    TrackRefitter = cms.InputTag("generalTracks"),
    beamSpotInputTag = cms.InputTag("offlineBeamSpot"),
    newSeedCandidates = cms.string('conv2SeedCandidates'),
    primaryVerticesTag = cms.InputTag("pixelVertices"),
    xcheckSeedCandidates = cms.string('xcheckSeedCandidates')
)


process.photonConvTrajSeedFromSingleLeg = cms.EDProducer("PhotonConversionTrajectorySeedProducerFromSingleLeg",
    ClusterCheckPSet = cms.PSet(
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(400000),
        MaxNumberOfPixelClusters = cms.uint32(40000),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
        doClusterCheck = cms.bool(True)
    ),
    DoxcheckSeedCandidates = cms.bool(False),
    OrderedHitsFactoryPSet = cms.PSet(
        SeedingLayers = cms.InputTag("convLayerPairs"),
        maxElement = cms.uint32(40000),
        maxHitPairsPerTrackAndGenerator = cms.uint32(10)
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
        RegionPSet = cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originHalfLength = cms.double(12.0),
            originRadius = cms.double(3.0),
            precise = cms.bool(True),
            ptMin = cms.double(0.2)
        )
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedForPhotonConversion1Leg'),
        SeedMomentumForBOFF = cms.double(5.0),
        TTRHBuilder = cms.string('WithTrackAngle'),
        propagator = cms.string('PropagatorWithMaterial')
    ),
    TrackRefitter = cms.InputTag("generalTracks"),
    applyTkVtxConstraint = cms.bool(True),
    beamSpotInputTag = cms.InputTag("offlineBeamSpot"),
    maxDZSigmas = cms.double(10.0),
    maxNumSelVtx = cms.uint32(2),
    newSeedCandidates = cms.string('convSeedCandidates'),
    primaryVerticesTag = cms.InputTag("firstStepPrimaryVertices"),
    vtxMinDoF = cms.double(4),
    xcheckSeedCandidates = cms.string('xcheckSeedCandidates')
)


process.pixelLessLayerPairs4PixelLessTracking = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(

    ),
    FPix = cms.PSet(

    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        useRingSlector = cms.bool(True),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TIB = cms.PSet(

    ),
    TIB1 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TIB2 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TIB3 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TID = cms.PSet(

    ),
    TID1 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(3),
        minRing = cms.int32(1),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        useRingSlector = cms.bool(True),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TID2 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(3),
        minRing = cms.int32(1),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        useRingSlector = cms.bool(True),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TID3 = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHitUnmatched"),
        stereoRecHits = cms.InputTag("siStripMatchedRecHits","stereoRecHitUnmatched"),
        useRingSlector = cms.bool(True),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring(
        'TIB1+TIB2', 
        'TIB1+TIB3', 
        'TIB2+TIB3', 
        'TIB1+TID1_pos', 
        'TIB1+TID1_neg', 
        'TIB2+TID1_pos', 
        'TIB2+TID1_neg', 
        'TIB1+TID2_pos', 
        'TIB1+TID2_neg', 
        'TID1_pos+TID2_pos', 
        'TID2_pos+TID3_pos', 
        'TID3_pos+TEC2_pos', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TID1_neg+TID2_neg', 
        'TID2_neg+TID3_neg', 
        'TID3_neg+TEC2_neg', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg'
    )
)


process.pixelLessStep = cms.EDProducer("ClassifierMerger",
    inputClassifiers = cms.vstring(
        'pixelLessStepClassifier1', 
        'pixelLessStepClassifier2'
    )
)


process.pixelLessStepClassifier1 = cms.EDProducer("TrackMVAClassifierPrompt",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorIter5_13TeV')
    ),
    qualityCuts = cms.vdouble(-0.4, 0.0, 0.4),
    src = cms.InputTag("pixelLessStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.pixelLessStepClassifier2 = cms.EDProducer("TrackMVAClassifierPrompt",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorIter0_13TeV')
    ),
    qualityCuts = cms.vdouble(-0.0, 0.0, 0.0),
    src = cms.InputTag("pixelLessStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.pixelLessStepClusters = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag("mixedTripletStepClusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trackClassifier = cms.InputTag("mixedTripletStep","QualityMasks"),
    trajectories = cms.InputTag("mixedTripletStepTracks")
)


process.pixelLessStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(50000000),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("pixelLessStepSeedLayers"),
    trackingRegions = cms.InputTag("pixelLessStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.pixelLessStepHitTriplets = cms.EDProducer("MultiHitFromChi2EDProducer",
    ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    chi2VsPtCut = cms.bool(True),
    chi2_cuts = cms.vdouble(3, 4, 5, 5),
    detIdsToDebug = cms.vint32(0, 0, 0),
    doublets = cms.InputTag("pixelLessStepHitDoublets"),
    extraHitRPhitolerance = cms.double(0),
    extraHitRZtolerance = cms.double(0),
    extraPhiKDBox = cms.double(0.005),
    extraRKDBox = cms.double(0.2),
    extraZKDBox = cms.double(0.2),
    fnSigmaRZ = cms.double(2),
    maxChi2 = cms.double(5),
    maxElement = cms.uint32(1000000),
    phiPreFiltering = cms.double(0.3),
    pt_interv = cms.vdouble(0.4, 0.7, 1, 2),
    refitHits = cms.bool(True),
    useFixedPreFiltering = cms.bool(False)
)


process.pixelLessStepMasks = cms.EDProducer("FastTrackerRecHitMaskProducer",
    TrackQuality = cms.string('highPurity'),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    minNumberOfLayersWithMeasBeforeFiltering_ = cms.int32(0),
    oldHitRemovalInfo = cms.InputTag("mixedTripletStepMasks"),
    recHits = cms.InputTag("fastTrackerRecHits"),
    trackClassifier = cms.InputTag("mixedTripletStep","QualityMasks"),
    trackQuality = cms.string('hightPurity'),
    trajectories = cms.InputTag("mixedTripletStepTracks")
)


process.pixelLessStepSeedClusterMask = cms.EDProducer("SeedClusterRemover",
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    oldClusterRemovalInfo = cms.InputTag("mixedTripletStepSeedClusterMask"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trajectories = cms.InputTag("pixelLessStepSeeds")
)


process.pixelLessStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    MTEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(3),
        minRing = cms.int32(3),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"),
        useRingSlector = cms.bool(True)
    ),
    MTIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters")
    ),
    MTID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(3),
        minRing = cms.int32(3),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters"),
        useRingSlector = cms.bool(True)
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("pixelLessStepClusters"),
        useRingSlector = cms.bool(True)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        skipClusters = cms.InputTag("pixelLessStepClusters")
    ),
    TID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("pixelLessStepClusters"),
        useRingSlector = cms.bool(True)
    ),
    layerList = cms.vstring(
        'TIB1+TIB2+MTIB3', 
        'TIB1+TIB2+MTIB4', 
        'TIB1+TIB2+MTID1_pos', 
        'TIB1+TIB2+MTID1_neg', 
        'TID1_pos+TID2_pos+TID3_pos', 
        'TID1_neg+TID2_neg+TID3_neg', 
        'TID1_pos+TID2_pos+MTID3_pos', 
        'TID1_neg+TID2_neg+MTID3_neg', 
        'TID1_pos+TID2_pos+MTEC1_pos', 
        'TID1_neg+TID2_neg+MTEC1_neg', 
        'TID2_pos+TID3_pos+TEC1_pos', 
        'TID2_neg+TID3_neg+TEC1_neg', 
        'TID2_pos+TID3_pos+MTEC1_pos', 
        'TID2_neg+TID3_neg+MTEC1_neg', 
        'TEC1_pos+TEC2_pos+TEC3_pos', 
        'TEC1_neg+TEC2_neg+TEC3_neg', 
        'TEC1_pos+TEC2_pos+MTEC3_pos', 
        'TEC1_neg+TEC2_neg+MTEC3_neg', 
        'TEC1_pos+TEC2_pos+TEC4_pos', 
        'TEC1_neg+TEC2_neg+TEC4_neg', 
        'TEC1_pos+TEC2_pos+MTEC4_pos', 
        'TEC1_neg+TEC2_neg+MTEC4_neg', 
        'TEC2_pos+TEC3_pos+TEC4_pos', 
        'TEC2_neg+TEC3_neg+TEC4_neg', 
        'TEC2_pos+TEC3_pos+MTEC4_pos', 
        'TEC2_neg+TEC3_neg+MTEC4_neg', 
        'TEC2_pos+TEC3_pos+TEC5_pos', 
        'TEC2_neg+TEC3_neg+TEC5_neg', 
        'TEC2_pos+TEC3_pos+TEC6_pos', 
        'TEC2_neg+TEC3_neg+TEC6_neg', 
        'TEC3_pos+TEC4_pos+TEC5_pos', 
        'TEC3_neg+TEC4_neg+TEC5_neg', 
        'TEC3_pos+TEC4_pos+MTEC5_pos', 
        'TEC3_neg+TEC4_neg+MTEC5_neg', 
        'TEC3_pos+TEC5_pos+TEC6_pos', 
        'TEC3_neg+TEC5_neg+TEC6_neg', 
        'TEC4_pos+TEC5_pos+TEC6_pos', 
        'TEC4_neg+TEC5_neg+TEC6_neg'
    )
)


process.pixelLessStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
                ClusterShapeHitFilterName = cms.string('pixelLessStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("pixelLessStepHitTriplets")
)


process.pixelLessStepSelector = cms.EDProducer("MultiTrackSelector",
    GBRForestLabel = cms.string('MVASelectorIter5'),
    beamspot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("pixelLessStepTracks"),
    trackSelectors = cms.VPSet(
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.5),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(1.3, 4.0),
            d0_par2 = cms.vdouble(1.3, 4.0),
            dz_par1 = cms.vdouble(1.3, 4.0),
            dz_par2 = cms.vdouble(1.3, 4.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(1),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(4),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('pixelLessStepLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.35),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(1.1, 4.0),
            d0_par2 = cms.vdouble(1.1, 4.0),
            dz_par1 = cms.vdouble(1.1, 4.0),
            dz_par2 = cms.vdouble(1.1, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(0),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(4),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('pixelLessStepTight'),
            preFilterName = cms.string('pixelLessStepLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.2),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.9, 4.0),
            d0_par2 = cms.vdouble(0.9, 4.0),
            dz_par1 = cms.vdouble(0.9, 4.0),
            dz_par2 = cms.vdouble(0.9, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(0),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(4),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('QualityMasks'),
            preFilterName = cms.string('pixelLessStepTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        )
    ),
    useAnyMVA = cms.bool(False),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertices = cms.InputTag("pixelVertices")
)


process.pixelLessStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('pixelLessStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('pixelLessStepTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("pixelLessStepClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("pixelLessStepSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.pixelLessStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(0),
        originHalfLength = cms.double(12.0),
        originRadius = cms.double(1.0),
        precise = cms.bool(True),
        ptMin = cms.double(0.4),
        useMultipleScattering = cms.bool(False)
    )
)


process.pixelLessStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('pixelLessStep'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("pixelLessStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.pixelPairElectronHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(1000000),
    maxElementTotal = cms.uint32(12000000),
    produceIntermediateHitDoublets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    seedingLayers = cms.InputTag("pixelPairElectronSeedLayers"),
    trackingRegions = cms.InputTag("pixelPairElectronTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.pixelPairElectronSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("tripletElectronClusterMask")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("tripletElectronClusterMask")
    ),
    layerList = cms.vstring(
        'BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg'
    )
)


process.pixelPairElectronSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("pixelPairElectronHitDoublets")
)


process.pixelPairElectronTrackingRegions = cms.EDProducer("GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet(
        VertexCollection = cms.InputTag("firstStepPrimaryVertices"),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        fixedError = cms.double(0.03),
        halfLengthScaling4BigEvts = cms.bool(False),
        maxNVertices = cms.int32(-1),
        maxPtMin = cms.double(1000),
        minHalfLength = cms.double(0),
        minOriginR = cms.double(0),
        nSigmaZ = cms.double(4),
        originRScaling4BigEvts = cms.bool(False),
        originRadius = cms.double(0.015),
        pixelClustersForScaling = cms.InputTag("siPixelClusters"),
        precise = cms.bool(True),
        ptMin = cms.double(1.0),
        ptMinScaling4BigEvts = cms.bool(False),
        scalingEndNPix = cms.double(1),
        scalingStartNPix = cms.double(0),
        sigmaZVertex = cms.double(3),
        useFakeVertices = cms.bool(False),
        useFixedError = cms.bool(True),
        useFoundVertices = cms.bool(True),
        useMultipleScattering = cms.bool(False)
    )
)


process.pixelPairStep = cms.EDProducer("TrackMVAClassifierPrompt",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorIter2_13TeV')
    ),
    qualityCuts = cms.vdouble(-0.2, 0.0, 0.3),
    src = cms.InputTag("pixelPairStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.pixelPairStepClusters = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag("lowPtTripletStepClusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trackClassifier = cms.InputTag("lowPtTripletStep","QualityMasks"),
    trajectories = cms.InputTag("lowPtTripletStepTracks")
)


process.pixelPairStepHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(1000000),
    maxElementTotal = cms.uint32(12000000),
    produceIntermediateHitDoublets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    seedingLayers = cms.InputTag("pixelPairStepSeedLayers"),
    trackingRegions = cms.InputTag("pixelPairStepTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.pixelPairStepHitDoubletsB = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(1000000),
    maxElementTotal = cms.uint32(12000000),
    produceIntermediateHitDoublets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    seedingLayers = cms.InputTag(""),
    trackingRegions = cms.InputTag(""),
    trackingRegionsSeedingLayers = cms.InputTag("pixelPairStepTrackingRegionsSeedLayersB")
)


process.pixelPairStepMasks = cms.EDProducer("FastTrackerRecHitMaskProducer",
    TrackQuality = cms.string('highPurity'),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    minNumberOfLayersWithMeasBeforeFiltering_ = cms.int32(0),
    oldHitRemovalInfo = cms.InputTag("lowPtTripletStepMasks"),
    recHits = cms.InputTag("fastTrackerRecHits"),
    trackClassifier = cms.InputTag("lowPtTripletStep","QualityMasks"),
    trackQuality = cms.string('hightPurity'),
    trajectories = cms.InputTag("lowPtTripletStepTracks")
)


process.pixelPairStepSeedClusterMask = cms.EDProducer("SeedClusterRemover",
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    oldClusterRemovalInfo = cms.InputTag("initialStepSeedClusterMask"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trajectories = cms.InputTag("pixelPairStepSeeds")
)


process.pixelPairStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters")
    ),
    layerList = cms.vstring(
        'BPix1+BPix2', 
        'BPix1+BPix3', 
        'BPix2+BPix3', 
        'BPix1+FPix1_pos', 
        'BPix1+FPix1_neg', 
        'BPix2+FPix1_pos', 
        'BPix2+FPix1_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg'
    )
)


process.pixelPairStepSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(True),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("pixelPairStepHitDoublets")
)


process.pixelPairStepSeedsA = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(True),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("pixelPairStepHitDoublets")
)


process.pixelPairStepSeedsB = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
        ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
        ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
        FilterAtHelixStage = cms.bool(True),
        FilterPixelHits = cms.bool(True),
        FilterStripHits = cms.bool(False)
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("pixelPairStepHitDoubletsB")
)


process.pixelPairStepSelector = cms.EDProducer("MultiTrackSelector",
    GBRForestLabel = cms.string('MVASelectorIter2'),
    beamspot = cms.InputTag("offlineBeamSpot"),
    src = cms.InputTag("pixelPairStepTracks"),
    trackSelectors = cms.VPSet(
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(1.6),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.55, 4.0),
            d0_par2 = cms.vdouble(0.55, 4.0),
            dz_par1 = cms.vdouble(0.65, 4.0),
            dz_par2 = cms.vdouble(0.45, 4.0),
            keepAllTracks = cms.bool(False),
            maxNumberLostLayers = cms.uint32(999),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(0),
            minNumberLayers = cms.uint32(0),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('pixelPairStepLoose'),
            preFilterName = cms.string(''),
            qualityBit = cms.string('loose'),
            res_par = cms.vdouble(0.003, 0.01),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.7),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.3, 4.0),
            d0_par2 = cms.vdouble(0.4, 4.0),
            dz_par1 = cms.vdouble(0.35, 4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('pixelPairStepTight'),
            preFilterName = cms.string('pixelPairStepLoose'),
            qualityBit = cms.string('tight'),
            res_par = cms.vdouble(0.003, 0.01),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        ), 
        cms.PSet(
            applyAbsCutsIfNoPV = cms.bool(False),
            applyAdaptedPVCuts = cms.bool(True),
            chi2n_no1Dmod_par = cms.double(9999),
            chi2n_par = cms.double(0.7),
            copyExtras = cms.untracked.bool(True),
            copyTrajectories = cms.untracked.bool(False),
            d0_par1 = cms.vdouble(0.3, 4.0),
            d0_par2 = cms.vdouble(0.4, 4.0),
            dz_par1 = cms.vdouble(0.35, 4.0),
            dz_par2 = cms.vdouble(0.4, 4.0),
            keepAllTracks = cms.bool(True),
            maxNumberLostLayers = cms.uint32(2),
            max_d0 = cms.double(100.0),
            max_eta = cms.double(9999.0),
            max_lostHitFraction = cms.double(1.0),
            max_minMissHitOutOrIn = cms.int32(99),
            max_relpterr = cms.double(9999.0),
            max_z0 = cms.double(100.0),
            minHitsToBypassChecks = cms.uint32(20),
            minNumber3DLayers = cms.uint32(3),
            minNumberLayers = cms.uint32(3),
            min_eta = cms.double(-9999.0),
            min_nhits = cms.uint32(0),
            nSigmaZ = cms.double(4.0),
            name = cms.string('QualityMasks'),
            preFilterName = cms.string('pixelPairStepTight'),
            qualityBit = cms.string('highPurity'),
            res_par = cms.vdouble(0.003, 0.001),
            vertexCut = cms.string('ndof>=2&!isFake'),
            vtxNumber = cms.int32(-1)
        )
    ),
    useAnyMVA = cms.bool(True),
    useVertices = cms.bool(True),
    useVtxError = cms.bool(False),
    vertices = cms.InputTag("pixelVertices")
)


process.pixelPairStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('pixelPairStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("pixelPairStepClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("pixelPairStepSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.pixelPairStepTrackingRegions = cms.EDProducer("GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet(
        VertexCollection = cms.InputTag("firstStepPrimaryVertices"),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        fixedError = cms.double(0.03),
        halfLengthScaling4BigEvts = cms.bool(False),
        maxNVertices = cms.int32(-1),
        maxPtMin = cms.double(1000),
        minHalfLength = cms.double(0),
        minOriginR = cms.double(0),
        nSigmaZ = cms.double(4),
        originRScaling4BigEvts = cms.bool(False),
        originRadius = cms.double(0.015),
        pixelClustersForScaling = cms.InputTag("siPixelClusters"),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        ptMinScaling4BigEvts = cms.bool(False),
        scalingEndNPix = cms.double(1),
        scalingStartNPix = cms.double(0),
        sigmaZVertex = cms.double(3),
        useFakeVertices = cms.bool(False),
        useFixedError = cms.bool(True),
        useFoundVertices = cms.bool(True),
        useMultipleScattering = cms.bool(True)
    )
)


process.pixelPairStepTrackingRegionsSeedLayersB = cms.EDProducer("PixelInactiveAreaTrackingRegionsSeedingLayersProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('WithTrackAngle'),
        skipClusters = cms.InputTag("pixelPairStepClusters")
    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        deltaEta_Cand = cms.double(-1),
        deltaPhi_Cand = cms.double(-1),
        extraEta = cms.double(0),
        extraPhi = cms.double(0),
        input = cms.InputTag(""),
        maxNVertices = cms.int32(5),
        measurementTrackerName = cms.InputTag(""),
        nSigmaZBeamSpot = cms.double(4),
        nSigmaZVertex = cms.double(3),
        operationMode = cms.string('VerticesFixed'),
        originRadius = cms.double(0.015),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        searchOpt = cms.bool(False),
        seedingMode = cms.string('Global'),
        vertexCollection = cms.InputTag("firstStepPrimaryVertices"),
        whereToUseMeasurementTracker = cms.string('Never'),
        zErrorBeamSpot = cms.double(24.2),
        zErrorVertex = cms.double(0.03)
    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    badPixelFEDChannelCollectionLabels = cms.VInputTag("siPixelDigis"),
    createPlottingFiles = cms.untracked.bool(False),
    debug = cms.untracked.bool(False),
    ignoreSingleFPixPanelModules = cms.bool(True),
    inactivePixelDetectorLabels = cms.VInputTag("siPixelDigis"),
    layerList = cms.vstring(
        'BPix1+BPix4', 
        'BPix2+BPix4', 
        'BPix3+BPix4', 
        'BPix1+FPix2_pos', 
        'BPix1+FPix2_neg', 
        'BPix1+FPix3_pos', 
        'BPix1+FPix3_neg', 
        'BPix2+FPix2_pos', 
        'BPix2+FPix2_neg', 
        'BPix3+FPix1_pos', 
        'BPix3+FPix1_neg', 
        'FPix1_pos+FPix2_pos', 
        'FPix1_neg+FPix2_neg', 
        'FPix1_pos+FPix3_pos', 
        'FPix1_neg+FPix3_neg', 
        'FPix2_pos+FPix3_pos', 
        'FPix2_neg+FPix3_neg'
    )
)


process.pixelPairStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('pixelPairStep'),
    Fitter = cms.string('FlexibleKFFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("pixelPairStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.preDuplicateMergingGeneralTracks = cms.EDProducer("TrackCollectionMerger",
    allowFirstHitShare = cms.bool(True),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    enableMerging = cms.bool(True),
    foundHitBonus = cms.double(100.0),
    inputClassifiers = cms.vstring(
        'earlyGeneralTracks', 
        'muonSeededTracksInOutClassifier', 
        'muonSeededTracksOutInClassifier'
    ),
    lostHitPenalty = cms.double(1.0),
    minQuality = cms.string('loose'),
    minShareHits = cms.uint32(2),
    shareFrac = cms.double(0.19),
    trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
    trackProducers = cms.VInputTag("earlyGeneralTracks", "muonSeededTracksInOut", "muonSeededTracksOutIn")
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.regionalCosmicCkfTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('CosmicNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('GroupedCkfTrajectoryBuilderP5')
    ),
    TrajectoryCleaner = cms.string('TrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("regionalCosmicTrackerSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.regionalCosmicTrackerSeedingLayers = cms.EDProducer("SeedingLayersEDProducer",
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        maxRing = cms.int32(7),
        minRing = cms.int32(6),
        useRingSlector = cms.bool(False)
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        )
    ),
    layerList = cms.vstring(
        'TOB6+TOB5', 
        'TOB6+TOB4', 
        'TOB6+TOB3', 
        'TOB5+TOB4', 
        'TOB5+TOB3', 
        'TOB4+TOB3', 
        'TEC1_neg+TOB6', 
        'TEC1_neg+TOB5', 
        'TEC1_neg+TOB4', 
        'TEC1_pos+TOB6', 
        'TEC1_pos+TOB5', 
        'TEC1_pos+TOB4'
    )
)


process.regionalCosmicTrackerSeeds = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    ClusterCheckPSet = cms.PSet(
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(10000),
        MaxNumberOfPixelClusters = cms.uint32(10000),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        doClusterCheck = cms.bool(False)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string('GenericPairGenerator'),
        LayerSrc = cms.InputTag("regionalCosmicTrackerSeedingLayers")
    ),
    RegionFactoryPSet = cms.PSet(
        CollectionsPSet = cms.PSet(
            recoL2MuonsCollection = cms.InputTag(""),
            recoMuonsCollection = cms.InputTag(""),
            recoTrackMuonsCollection = cms.InputTag("cosmicMuons")
        ),
        ComponentName = cms.string('CosmicRegionalSeedGenerator'),
        RegionInJetsCheckPSet = cms.PSet(
            deltaRExclusionSize = cms.double(0.3),
            doJetsExclusionCheck = cms.bool(True),
            jetsPtMin = cms.double(5),
            recoCaloJetsCollection = cms.InputTag("ak4CaloJets")
        ),
        RegionPSet = cms.PSet(
            deltaEtaRegion = cms.double(0.1),
            deltaPhiRegion = cms.double(0.1),
            measurementTrackerName = cms.string(''),
            precise = cms.bool(True),
            ptMin = cms.double(1.0),
            rVertex = cms.double(5),
            zVertex = cms.double(5)
        ),
        ToolsPSet = cms.PSet(
            regionBase = cms.string('seedOnCosmicMuon'),
            thePropagatorName = cms.string('AnalyticalPropagator')
        )
    ),
    RegionInJetsCheckPSet = cms.PSet(
        doJetsExclusionCheck = cms.bool(False)
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('CosmicSeedCreator'),
        MinOneOverPtError = cms.double(1.0),
        OriginTransverseErrorMultiplier = cms.double(1.0),
        SeedMomentumForBOFF = cms.double(5.0),
        TTRHBuilder = cms.string('WithTrackAngle'),
        forceKinematicWithRegionDirection = cms.bool(False),
        magneticField = cms.string('ParabolicMf'),
        maxseeds = cms.int32(10000),
        propagator = cms.string('PropagatorWithMaterialParabolicMf')
    )
)


process.regionalCosmicTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('ctf'),
    Fitter = cms.string('FittingSmootherRKP5'),
    GeometricInnerState = cms.bool(True),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("regionalCosmicCkfTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.seedClusterRemover = cms.EDProducer("SeedClusterRemover",
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trajectories = cms.InputTag("initialStepSeeds")
)


process.seedClusterRemoverPhase2 = cms.EDProducer("SeedClusterRemoverPhase2",
    phase2OTClusters = cms.InputTag("siPhase2Clusters"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    trajectories = cms.InputTag("initialStepSeeds")
)


process.seedGeneratorFromRegionHitsEDProducer = cms.EDProducer("SeedGeneratorFromRegionHitsEDProducer",
    ClusterCheckPSet = cms.PSet(
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        MaxNumberOfCosmicClusters = cms.uint32(400000),
        MaxNumberOfPixelClusters = cms.uint32(40000),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
        doClusterCheck = cms.bool(True)
    ),
    OrderedHitsFactoryPSet = cms.PSet(
        ComponentName = cms.string(''),
        SeedingLayers = cms.InputTag(""),
        maxElement = cms.uint32(1000000)
    ),
    RegionFactoryPSet = cms.PSet(
        ComponentName = cms.string('GlobalRegionProducerFromBeamSpot'),
        RegionPSet = cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            originHalfLength = cms.double(21.2),
            originRadius = cms.double(0.2),
            precise = cms.bool(True),
            ptMin = cms.double(0.9),
            useMultipleScattering = cms.bool(False)
        )
    ),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedCreatorPSet = cms.PSet(
        ComponentName = cms.string('SeedFromConsecutiveHitsCreator'),
        MinOneOverPtError = cms.double(1.0),
        OriginTransverseErrorMultiplier = cms.double(1.0),
        SeedMomentumForBOFF = cms.double(5.0),
        TTRHBuilder = cms.string('WithTrackAngle'),
        forceKinematicWithRegionDirection = cms.bool(False),
        magneticField = cms.string('ParabolicMf'),
        propagator = cms.string('PropagatorWithMaterialParabolicMf')
    )
)


process.seedingLayersEDProducer = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(

    ),
    FPix = cms.PSet(

    ),
    MTEC = cms.PSet(

    ),
    MTIB = cms.PSet(

    ),
    MTID = cms.PSet(

    ),
    MTOB = cms.PSet(

    ),
    TEC = cms.PSet(

    ),
    TIB = cms.PSet(

    ),
    TID = cms.PSet(

    ),
    TOB = cms.PSet(

    ),
    layerList = cms.vstring()
)


process.siPixelClusterShapeCache = cms.EDProducer("SiPixelClusterShapeCacheProducer",
    onDemand = cms.bool(False),
    src = cms.InputTag("siPixelClusters")
)


process.siPixelClusters = cms.EDProducer("JetCoreClusterSplitter",
    centralMIPCharge = cms.double(26000),
    chargeFractionMin = cms.double(2.0),
    chargePerUnit = cms.double(2000),
    cores = cms.InputTag("jetsForCoreTrackingPreSplitting"),
    deltaRmax = cms.double(0.05),
    forceXError = cms.double(100),
    forceYError = cms.double(150),
    fractionalWidth = cms.double(0.4),
    pixelCPE = cms.string('PixelCPEGeneric'),
    pixelClusters = cms.InputTag("siPixelClustersPreSplitting"),
    ptMin = cms.double(200),
    verbose = cms.bool(False),
    vertices = cms.InputTag("firstStepPrimaryVerticesPreSplitting")
)


process.siPixelClustersBottom = cms.EDProducer("PixelClusterSelectorTopBottom",
    label = cms.InputTag("siPixelClusters"),
    y = cms.double(-1)
)


process.siPixelClustersTop = cms.EDProducer("PixelClusterSelectorTopBottom",
    label = cms.InputTag("siPixelClusters"),
    y = cms.double(1)
)


process.siPixelRecHits = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("siPixelClusters")
)


process.siPixelRecHitsBottom = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("siPixelClustersBottom")
)


process.siPixelRecHitsPreSplitting = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("siPixelClustersPreSplitting")
)


process.siPixelRecHitsTop = cms.EDProducer("SiPixelRecHitConverter",
    CPE = cms.string('PixelCPEGeneric'),
    VerboseLevel = cms.untracked.int32(0),
    src = cms.InputTag("siPixelClustersTop")
)


process.siStripClusters = cms.EDProducer("SiStripClusterizer",
    Clusterizer = cms.PSet(
        Algorithm = cms.string('ThreeThresholdAlgorithm'),
        ChannelThreshold = cms.double(2.0),
        ClusterThreshold = cms.double(5.0),
        MaxAdjacentBad = cms.uint32(0),
        MaxSequentialBad = cms.uint32(1),
        MaxSequentialHoles = cms.uint32(0),
        QualityLabel = cms.string(''),
        RemoveApvShots = cms.bool(True),
        SeedThreshold = cms.double(3.0),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        )
    ),
    DigiProducersList = cms.VInputTag(cms.InputTag("siStripDigis","ZeroSuppressed"), cms.InputTag("siStripZeroSuppression","VirginRaw"), cms.InputTag("siStripZeroSuppression","ProcessedRaw"), cms.InputTag("siStripZeroSuppression","ScopeMode"))
)


process.siStripClustersBottom = cms.EDProducer("StripClusterSelectorTopBottom",
    label = cms.InputTag("siStripClusters"),
    y = cms.double(-1)
)


process.siStripClustersTop = cms.EDProducer("StripClusterSelectorTopBottom",
    label = cms.InputTag("siStripClusters"),
    y = cms.double(1)
)


process.siStripMatchedRecHits = cms.EDProducer("SiStripRecHitConverter",
    ClusterProducer = cms.InputTag("siStripClusters"),
    MaskBadAPVFibers = cms.bool(False),
    Matcher = cms.ESInputTag("SiStripRecHitMatcherESProducer","StandardMatcher"),
    StripCPE = cms.ESInputTag("StripCPEfromTrackAngleESProducer","StripCPEfromTrackAngle"),
    VerbosityLevel = cms.untracked.int32(1),
    matchedRecHits = cms.string('matchedRecHit'),
    rphiRecHits = cms.string('rphiRecHit'),
    siStripQualityLabel = cms.ESInputTag(""),
    stereoRecHits = cms.string('stereoRecHit'),
    useSiStripQuality = cms.bool(False)
)


process.siStripMatchedRecHitsBottom = cms.EDProducer("SiStripRecHitConverter",
    ClusterProducer = cms.InputTag("siStripClustersBottom"),
    MaskBadAPVFibers = cms.bool(False),
    Matcher = cms.ESInputTag("SiStripRecHitMatcherESProducer","StandardMatcher"),
    StripCPE = cms.ESInputTag("StripCPEfromTrackAngleESProducer","StripCPEfromTrackAngle"),
    VerbosityLevel = cms.untracked.int32(1),
    matchedRecHits = cms.string('matchedRecHit'),
    rphiRecHits = cms.string('rphiRecHit'),
    siStripQualityLabel = cms.ESInputTag(""),
    stereoRecHits = cms.string('stereoRecHit'),
    useSiStripQuality = cms.bool(False)
)


process.siStripMatchedRecHitsTop = cms.EDProducer("SiStripRecHitConverter",
    ClusterProducer = cms.InputTag("siStripClustersTop"),
    MaskBadAPVFibers = cms.bool(False),
    Matcher = cms.ESInputTag("SiStripRecHitMatcherESProducer","StandardMatcher"),
    StripCPE = cms.ESInputTag("StripCPEfromTrackAngleESProducer","StripCPEfromTrackAngle"),
    VerbosityLevel = cms.untracked.int32(1),
    matchedRecHits = cms.string('matchedRecHit'),
    rphiRecHits = cms.string('rphiRecHit'),
    siStripQualityLabel = cms.ESInputTag(""),
    stereoRecHits = cms.string('stereoRecHit'),
    useSiStripQuality = cms.bool(False)
)


process.siStripZeroSuppression = cms.EDProducer("SiStripZeroSuppression",
    Algorithms = cms.PSet(
        APVInspectMode = cms.string('BaselineFollower'),
        APVRestoreMode = cms.string('BaselineFollower'),
        ApplyBaselineCleaner = cms.bool(True),
        ApplyBaselineRejection = cms.bool(True),
        CleaningSequence = cms.uint32(1),
        CommonModeNoiseSubtractionMode = cms.string('IteratedMedian'),
        CutToAvoidSignal = cms.double(2.0),
        DeltaCMThreshold = cms.uint32(20),
        Deviation = cms.uint32(25),
        ForceNoRestore = cms.bool(False),
        Fraction = cms.double(0.2),
        Iterations = cms.int32(3),
        MeanCM = cms.int32(0),
        PedestalSubtractionFedMode = cms.bool(False),
        SiStripFedZeroSuppressionMode = cms.uint32(4),
        TruncateInSuppressor = cms.bool(True),
        Use10bitsTruncation = cms.bool(False),
        consecThreshold = cms.uint32(5),
        discontinuityThreshold = cms.int32(12),
        distortionThreshold = cms.uint32(20),
        doAPVRestore = cms.bool(True),
        filteredBaselineDerivativeSumSquare = cms.double(30),
        filteredBaselineMax = cms.double(6),
        hitStripThreshold = cms.uint32(40),
        lastGradient = cms.int32(10),
        minStripsToFit = cms.uint32(4),
        nSaturatedStrip = cms.uint32(2),
        nSigmaNoiseDerTh = cms.uint32(4),
        nSmooth = cms.uint32(9),
        restoreThreshold = cms.double(0.5),
        sizeWindow = cms.int32(1),
        slopeX = cms.int32(3),
        slopeY = cms.int32(4),
        useCMMeanMap = cms.bool(False),
        useRealMeanCM = cms.bool(False),
        widthCluster = cms.int32(64)
    ),
    RawDigiProducersList = cms.VInputTag(cms.InputTag("siStripDigis","VirginRaw"), cms.InputTag("siStripDigis","ProcessedRaw"), cms.InputTag("siStripDigis","ScopeMode")),
    fixCM = cms.bool(False),
    produceBaselinePoints = cms.bool(False),
    produceCalculatedBaseline = cms.bool(False),
    produceHybridFormat = cms.bool(False),
    produceRawDigis = cms.bool(True),
    storeCM = cms.bool(True),
    storeInZScollBadAPV = cms.bool(True)
)


process.simpleCosmicBONSeedingLayers = cms.EDProducer("SeedingLayersEDProducer",
    MTIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    ),
    MTOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit")
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(5),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        useRingSlector = cms.bool(False),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit")
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit")
    ),
    layerList = cms.vstring(
        'MTOB4+MTOB5+MTOB6', 
        'MTOB3+MTOB5+MTOB6', 
        'MTOB3+MTOB4+MTOB5', 
        'MTOB3+MTOB4+MTOB6', 
        'TOB2+MTOB4+MTOB5', 
        'TOB2+MTOB3+MTOB5', 
        'TEC7_pos+TEC8_pos+TEC9_pos', 
        'TEC6_pos+TEC7_pos+TEC8_pos', 
        'TEC5_pos+TEC6_pos+TEC7_pos', 
        'TEC4_pos+TEC5_pos+TEC6_pos', 
        'TEC3_pos+TEC4_pos+TEC5_pos', 
        'TEC2_pos+TEC3_pos+TEC4_pos', 
        'TEC1_pos+TEC2_pos+TEC3_pos', 
        'TEC7_neg+TEC8_neg+TEC9_neg', 
        'TEC6_neg+TEC7_neg+TEC8_neg', 
        'TEC5_neg+TEC6_neg+TEC7_neg', 
        'TEC4_neg+TEC5_neg+TEC6_neg', 
        'TEC3_neg+TEC4_neg+TEC5_neg', 
        'TEC2_neg+TEC3_neg+TEC4_neg', 
        'TEC1_neg+TEC2_neg+TEC3_neg', 
        'TEC6_pos+TEC8_pos+TEC9_pos', 
        'TEC5_pos+TEC7_pos+TEC8_pos', 
        'TEC4_pos+TEC6_pos+TEC7_pos', 
        'TEC3_pos+TEC5_pos+TEC6_pos', 
        'TEC2_pos+TEC4_pos+TEC5_pos', 
        'TEC1_pos+TEC3_pos+TEC4_pos', 
        'TEC6_pos+TEC7_pos+TEC9_pos', 
        'TEC5_pos+TEC6_pos+TEC8_pos', 
        'TEC4_pos+TEC5_pos+TEC7_pos', 
        'TEC3_pos+TEC4_pos+TEC6_pos', 
        'TEC2_pos+TEC3_pos+TEC5_pos', 
        'TEC1_pos+TEC2_pos+TEC4_pos', 
        'TEC6_neg+TEC8_neg+TEC9_neg', 
        'TEC5_neg+TEC7_neg+TEC8_neg', 
        'TEC4_neg+TEC6_neg+TEC7_neg', 
        'TEC3_neg+TEC5_neg+TEC6_neg', 
        'TEC2_neg+TEC4_neg+TEC5_neg', 
        'TEC1_neg+TEC3_neg+TEC4_neg', 
        'TEC6_neg+TEC7_neg+TEC9_neg', 
        'TEC5_neg+TEC6_neg+TEC8_neg', 
        'TEC4_neg+TEC5_neg+TEC7_neg', 
        'TEC3_neg+TEC4_neg+TEC6_neg', 
        'TEC2_neg+TEC3_neg+TEC5_neg', 
        'TEC1_neg+TEC2_neg+TEC4_neg', 
        'MTOB6+TEC1_pos+TEC2_pos', 
        'MTOB6+TEC1_neg+TEC2_neg', 
        'MTOB6+MTOB5+TEC1_pos', 
        'MTOB6+MTOB5+TEC1_neg'
    )
)


process.simpleCosmicBONSeedingLayersBottom = cms.EDProducer("SeedingLayersEDProducer",
    MTIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
    ),
    MTOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit")
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(5),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
        useRingSlector = cms.bool(False),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit")
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsBottom","matchedRecHit")
    ),
    layerList = cms.vstring(
        'MTOB4+MTOB5+MTOB6', 
        'MTOB3+MTOB5+MTOB6', 
        'MTOB3+MTOB4+MTOB5', 
        'MTOB3+MTOB4+MTOB6', 
        'TOB2+MTOB4+MTOB5', 
        'TOB2+MTOB3+MTOB5', 
        'TEC7_pos+TEC8_pos+TEC9_pos', 
        'TEC6_pos+TEC7_pos+TEC8_pos', 
        'TEC5_pos+TEC6_pos+TEC7_pos', 
        'TEC4_pos+TEC5_pos+TEC6_pos', 
        'TEC3_pos+TEC4_pos+TEC5_pos', 
        'TEC2_pos+TEC3_pos+TEC4_pos', 
        'TEC1_pos+TEC2_pos+TEC3_pos', 
        'TEC7_neg+TEC8_neg+TEC9_neg', 
        'TEC6_neg+TEC7_neg+TEC8_neg', 
        'TEC5_neg+TEC6_neg+TEC7_neg', 
        'TEC4_neg+TEC5_neg+TEC6_neg', 
        'TEC3_neg+TEC4_neg+TEC5_neg', 
        'TEC2_neg+TEC3_neg+TEC4_neg', 
        'TEC1_neg+TEC2_neg+TEC3_neg', 
        'TEC6_pos+TEC8_pos+TEC9_pos', 
        'TEC5_pos+TEC7_pos+TEC8_pos', 
        'TEC4_pos+TEC6_pos+TEC7_pos', 
        'TEC3_pos+TEC5_pos+TEC6_pos', 
        'TEC2_pos+TEC4_pos+TEC5_pos', 
        'TEC1_pos+TEC3_pos+TEC4_pos', 
        'TEC6_pos+TEC7_pos+TEC9_pos', 
        'TEC5_pos+TEC6_pos+TEC8_pos', 
        'TEC4_pos+TEC5_pos+TEC7_pos', 
        'TEC3_pos+TEC4_pos+TEC6_pos', 
        'TEC2_pos+TEC3_pos+TEC5_pos', 
        'TEC1_pos+TEC2_pos+TEC4_pos', 
        'TEC6_neg+TEC8_neg+TEC9_neg', 
        'TEC5_neg+TEC7_neg+TEC8_neg', 
        'TEC4_neg+TEC6_neg+TEC7_neg', 
        'TEC3_neg+TEC5_neg+TEC6_neg', 
        'TEC2_neg+TEC4_neg+TEC5_neg', 
        'TEC1_neg+TEC3_neg+TEC4_neg', 
        'TEC6_neg+TEC7_neg+TEC9_neg', 
        'TEC5_neg+TEC6_neg+TEC8_neg', 
        'TEC4_neg+TEC5_neg+TEC7_neg', 
        'TEC3_neg+TEC4_neg+TEC6_neg', 
        'TEC2_neg+TEC3_neg+TEC5_neg', 
        'TEC1_neg+TEC2_neg+TEC4_neg', 
        'MTOB6+TEC1_pos+TEC2_pos', 
        'MTOB6+TEC1_neg+TEC2_neg', 
        'MTOB6+MTOB5+TEC1_pos', 
        'MTOB6+MTOB5+TEC1_neg'
    )
)


process.simpleCosmicBONSeedingLayersTop = cms.EDProducer("SeedingLayersEDProducer",
    MTIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
    ),
    MTOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit")
    ),
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit"),
        maxRing = cms.int32(7),
        minRing = cms.int32(5),
        rphiRecHits = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
        useRingSlector = cms.bool(False),
        useSimpleRphiHitsCleaner = cms.bool(False)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit")
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHitsTop","matchedRecHit")
    ),
    layerList = cms.vstring(
        'MTOB4+MTOB5+MTOB6', 
        'MTOB3+MTOB5+MTOB6', 
        'MTOB3+MTOB4+MTOB5', 
        'MTOB3+MTOB4+MTOB6', 
        'TOB2+MTOB4+MTOB5', 
        'TOB2+MTOB3+MTOB5', 
        'TEC7_pos+TEC8_pos+TEC9_pos', 
        'TEC6_pos+TEC7_pos+TEC8_pos', 
        'TEC5_pos+TEC6_pos+TEC7_pos', 
        'TEC4_pos+TEC5_pos+TEC6_pos', 
        'TEC3_pos+TEC4_pos+TEC5_pos', 
        'TEC2_pos+TEC3_pos+TEC4_pos', 
        'TEC1_pos+TEC2_pos+TEC3_pos', 
        'TEC7_neg+TEC8_neg+TEC9_neg', 
        'TEC6_neg+TEC7_neg+TEC8_neg', 
        'TEC5_neg+TEC6_neg+TEC7_neg', 
        'TEC4_neg+TEC5_neg+TEC6_neg', 
        'TEC3_neg+TEC4_neg+TEC5_neg', 
        'TEC2_neg+TEC3_neg+TEC4_neg', 
        'TEC1_neg+TEC2_neg+TEC3_neg', 
        'TEC6_pos+TEC8_pos+TEC9_pos', 
        'TEC5_pos+TEC7_pos+TEC8_pos', 
        'TEC4_pos+TEC6_pos+TEC7_pos', 
        'TEC3_pos+TEC5_pos+TEC6_pos', 
        'TEC2_pos+TEC4_pos+TEC5_pos', 
        'TEC1_pos+TEC3_pos+TEC4_pos', 
        'TEC6_pos+TEC7_pos+TEC9_pos', 
        'TEC5_pos+TEC6_pos+TEC8_pos', 
        'TEC4_pos+TEC5_pos+TEC7_pos', 
        'TEC3_pos+TEC4_pos+TEC6_pos', 
        'TEC2_pos+TEC3_pos+TEC5_pos', 
        'TEC1_pos+TEC2_pos+TEC4_pos', 
        'TEC6_neg+TEC8_neg+TEC9_neg', 
        'TEC5_neg+TEC7_neg+TEC8_neg', 
        'TEC4_neg+TEC6_neg+TEC7_neg', 
        'TEC3_neg+TEC5_neg+TEC6_neg', 
        'TEC2_neg+TEC4_neg+TEC5_neg', 
        'TEC1_neg+TEC3_neg+TEC4_neg', 
        'TEC6_neg+TEC7_neg+TEC9_neg', 
        'TEC5_neg+TEC6_neg+TEC8_neg', 
        'TEC4_neg+TEC5_neg+TEC7_neg', 
        'TEC3_neg+TEC4_neg+TEC6_neg', 
        'TEC2_neg+TEC3_neg+TEC5_neg', 
        'TEC1_neg+TEC2_neg+TEC4_neg', 
        'MTOB6+TEC1_pos+TEC2_pos', 
        'MTOB6+TEC1_neg+TEC2_neg', 
        'MTOB6+MTOB5+TEC1_pos', 
        'MTOB6+MTOB5+TEC1_neg'
    )
)


process.simpleCosmicBONSeeds = cms.EDProducer("SimpleCosmicBONSeeder",
    ClusterChargeCheck = cms.PSet(
        Thresholds = cms.PSet(
            TEC = cms.int32(0),
            TIB = cms.int32(0),
            TID = cms.int32(0),
            TOB = cms.int32(0)
        ),
        checkCharge = cms.bool(False),
        matchedRecHitsUseAnd = cms.bool(True)
    ),
    ClusterCheckPSet = cms.PSet(
        ClusterCollectionLabel = cms.InputTag("siStripClusters"),
        DontCountDetsAboveNClusters = cms.uint32(20),
        MaxNumberOfCosmicClusters = cms.uint32(300),
        MaxNumberOfPixelClusters = cms.uint32(300),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        doClusterCheck = cms.bool(True)
    ),
    HitsPerModuleCheck = cms.PSet(
        Thresholds = cms.PSet(
            TEC = cms.int32(20),
            TIB = cms.int32(20),
            TID = cms.int32(20),
            TOB = cms.int32(20)
        ),
        checkHitsPerModule = cms.bool(True)
    ),
    NegativeYOnly = cms.bool(False),
    PositiveYOnly = cms.bool(False),
    RegionPSet = cms.PSet(
        originHalfLength = cms.double(90.0),
        originRadius = cms.double(150.0),
        originZPosition = cms.double(0.0),
        pMin = cms.double(1.0),
        ptMin = cms.double(0.5)
    ),
    TTRHBuilder = cms.string('WithTrackAngle'),
    TripletsDebugLevel = cms.untracked.uint32(0),
    TripletsSrc = cms.InputTag("simpleCosmicBONSeedingLayers"),
    helixDebugLevel = cms.untracked.uint32(0),
    maxSeeds = cms.int32(20000),
    maxTriplets = cms.int32(50000),
    minimumGoodHitsInSeed = cms.int32(3),
    rescaleError = cms.double(1.0),
    seedDebugLevel = cms.untracked.uint32(0),
    seedOnMiddle = cms.bool(False),
    writeTriplets = cms.bool(False)
)


process.simpleCosmicBONSeedsBottom = cms.EDProducer("SimpleCosmicBONSeeder",
    ClusterChargeCheck = cms.PSet(
        Thresholds = cms.PSet(
            TEC = cms.int32(0),
            TIB = cms.int32(0),
            TID = cms.int32(0),
            TOB = cms.int32(0)
        ),
        checkCharge = cms.bool(False),
        matchedRecHitsUseAnd = cms.bool(True)
    ),
    ClusterCheckPSet = cms.PSet(
        ClusterCollectionLabel = cms.InputTag("siStripClustersBottom"),
        DontCountDetsAboveNClusters = cms.uint32(20),
        MaxNumberOfCosmicClusters = cms.uint32(150),
        MaxNumberOfPixelClusters = cms.uint32(300),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        doClusterCheck = cms.bool(True)
    ),
    HitsPerModuleCheck = cms.PSet(
        Thresholds = cms.PSet(
            TEC = cms.int32(20),
            TIB = cms.int32(20),
            TID = cms.int32(20),
            TOB = cms.int32(20)
        ),
        checkHitsPerModule = cms.bool(True)
    ),
    NegativeYOnly = cms.bool(True),
    PositiveYOnly = cms.bool(False),
    RegionPSet = cms.PSet(
        originHalfLength = cms.double(90.0),
        originRadius = cms.double(150.0),
        originZPosition = cms.double(0.0),
        pMin = cms.double(1.0),
        ptMin = cms.double(0.5)
    ),
    TTRHBuilder = cms.string('WithTrackAngle'),
    TripletsDebugLevel = cms.untracked.uint32(0),
    TripletsSrc = cms.InputTag("simpleCosmicBONSeedingLayersBottom"),
    helixDebugLevel = cms.untracked.uint32(0),
    maxSeeds = cms.int32(20000),
    maxTriplets = cms.int32(50000),
    minimumGoodHitsInSeed = cms.int32(3),
    rescaleError = cms.double(1.0),
    seedDebugLevel = cms.untracked.uint32(0),
    seedOnMiddle = cms.bool(False),
    writeTriplets = cms.bool(False)
)


process.simpleCosmicBONSeedsTop = cms.EDProducer("SimpleCosmicBONSeeder",
    ClusterChargeCheck = cms.PSet(
        Thresholds = cms.PSet(
            TEC = cms.int32(0),
            TIB = cms.int32(0),
            TID = cms.int32(0),
            TOB = cms.int32(0)
        ),
        checkCharge = cms.bool(False),
        matchedRecHitsUseAnd = cms.bool(True)
    ),
    ClusterCheckPSet = cms.PSet(
        ClusterCollectionLabel = cms.InputTag("siStripClustersTop"),
        DontCountDetsAboveNClusters = cms.uint32(20),
        MaxNumberOfCosmicClusters = cms.uint32(150),
        MaxNumberOfPixelClusters = cms.uint32(300),
        PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
        doClusterCheck = cms.bool(True)
    ),
    HitsPerModuleCheck = cms.PSet(
        Thresholds = cms.PSet(
            TEC = cms.int32(20),
            TIB = cms.int32(20),
            TID = cms.int32(20),
            TOB = cms.int32(20)
        ),
        checkHitsPerModule = cms.bool(True)
    ),
    NegativeYOnly = cms.bool(False),
    PositiveYOnly = cms.bool(True),
    RegionPSet = cms.PSet(
        originHalfLength = cms.double(90.0),
        originRadius = cms.double(150.0),
        originZPosition = cms.double(0.0),
        pMin = cms.double(1.0),
        ptMin = cms.double(0.5)
    ),
    TTRHBuilder = cms.string('WithTrackAngle'),
    TripletsDebugLevel = cms.untracked.uint32(0),
    TripletsSrc = cms.InputTag("simpleCosmicBONSeedingLayersTop"),
    helixDebugLevel = cms.untracked.uint32(0),
    maxSeeds = cms.int32(20000),
    maxTriplets = cms.int32(50000),
    minimumGoodHitsInSeed = cms.int32(3),
    rescaleError = cms.double(1.0),
    seedDebugLevel = cms.untracked.uint32(0),
    seedOnMiddle = cms.bool(False),
    writeTriplets = cms.bool(False)
)


process.splittedTracksP5 = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('cosmic'),
    Fitter = cms.string('RKFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithTrackAngle'),
    TrajectoryInEvent = cms.bool(True),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("cosmicTrackSplitter"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.stripPairElectronHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(1000000),
    maxElementTotal = cms.uint32(12000000),
    produceIntermediateHitDoublets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    seedingLayers = cms.InputTag("stripPairElectronSeedLayers"),
    trackingRegions = cms.InputTag("stripPairElectronTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.stripPairElectronSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("tripletElectronClusterMask"),
        useRingSlector = cms.bool(True)
    ),
    TIB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        skipClusters = cms.InputTag("tripletElectronClusterMask")
    ),
    TID = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutNone')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(2),
        minRing = cms.int32(1),
        skipClusters = cms.InputTag("tripletElectronClusterMask"),
        useRingSlector = cms.bool(True)
    ),
    layerList = cms.vstring(
        'TIB1+TIB2', 
        'TIB1+TID1_pos', 
        'TIB1+TID1_neg', 
        'TID2_pos+TID3_pos', 
        'TID2_neg+TID3_neg', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TEC3_pos+TEC4_pos', 
        'TEC3_pos+TEC5_pos', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg', 
        'TEC3_neg+TEC4_neg', 
        'TEC3_neg+TEC5_neg'
    )
)


process.stripPairElectronSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("stripPairElectronHitDoublets")
)


process.stripPairElectronTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(0),
        originHalfLength = cms.double(12.0),
        originRadius = cms.double(0.4),
        precise = cms.bool(True),
        ptMin = cms.double(1.0),
        useMultipleScattering = cms.bool(False)
    )
)


process.tobTecStep = cms.EDProducer("ClassifierMerger",
    inputClassifiers = cms.vstring(
        'tobTecStepClassifier1', 
        'tobTecStepClassifier2'
    )
)


process.tobTecStepClassifier1 = cms.EDProducer("TrackMVAClassifierDetached",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorIter6_13TeV')
    ),
    qualityCuts = cms.vdouble(-0.6, -0.45, -0.3),
    src = cms.InputTag("tobTecStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.tobTecStepClassifier2 = cms.EDProducer("TrackMVAClassifierPrompt",
    beamspot = cms.InputTag("offlineBeamSpot"),
    ignoreVertices = cms.bool(False),
    mva = cms.PSet(
        GBRForestFileName = cms.string(''),
        GBRForestLabel = cms.string('MVASelectorIter0_13TeV')
    ),
    qualityCuts = cms.vdouble(0.0, 0.0, 0.0),
    src = cms.InputTag("tobTecStepTracks"),
    vertices = cms.InputTag("firstStepPrimaryVertices")
)


process.tobTecStepClusters = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(9.0),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepClusters"),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trackClassifier = cms.InputTag("pixelLessStep","QualityMasks"),
    trajectories = cms.InputTag("pixelLessStepTracks")
)


process.tobTecStepHitDoubletsPair = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(1000000),
    maxElementTotal = cms.uint32(12000000),
    produceIntermediateHitDoublets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    seedingLayers = cms.InputTag("tobTecStepSeedLayersPair"),
    trackingRegions = cms.InputTag("tobTecStepTrackingRegionsPair"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.tobTecStepHitDoubletsTripl = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(50000000),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("tobTecStepSeedLayersTripl"),
    trackingRegions = cms.InputTag("tobTecStepTrackingRegionsTripl"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.tobTecStepHitTripletsTripl = cms.EDProducer("MultiHitFromChi2EDProducer",
    ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter'),
    TTRHBuilder = cms.string('WithTrackAngle'),
    chi2VsPtCut = cms.bool(True),
    chi2_cuts = cms.vdouble(3, 4, 5, 5),
    detIdsToDebug = cms.vint32(0, 0, 0),
    doublets = cms.InputTag("tobTecStepHitDoubletsTripl"),
    extraHitRPhitolerance = cms.double(0),
    extraHitRZtolerance = cms.double(0),
    extraPhiKDBox = cms.double(0.01),
    extraRKDBox = cms.double(0.2),
    extraZKDBox = cms.double(0.2),
    fnSigmaRZ = cms.double(2),
    maxChi2 = cms.double(5),
    maxElement = cms.uint32(1000000),
    phiPreFiltering = cms.double(0.3),
    pt_interv = cms.vdouble(0.4, 0.7, 1, 2),
    refitHits = cms.bool(True),
    useFixedPreFiltering = cms.bool(False)
)


process.tobTecStepMasks = cms.EDProducer("FastTrackerRecHitMaskProducer",
    TrackQuality = cms.string('highPurity'),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    minNumberOfLayersWithMeasBeforeFiltering_ = cms.int32(0),
    oldHitRemovalInfo = cms.InputTag("pixelLessStepMasks"),
    recHits = cms.InputTag("fastTrackerRecHits"),
    trackClassifier = cms.InputTag("pixelLessStep","QualityMasks"),
    trackQuality = cms.string('hightPurity'),
    trajectories = cms.InputTag("pixelLessStepTracks")
)


process.tobTecStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTiny')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(5),
        minRing = cms.int32(5),
        skipClusters = cms.InputTag("tobTecStepClusters"),
        useRingSlector = cms.bool(True)
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTiny')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters")
    ),
    layerList = cms.vstring(
        'TOB1+TOB2', 
        'TOB1+TEC1_pos', 
        'TOB1+TEC1_neg', 
        'TEC1_pos+TEC2_pos', 
        'TEC2_pos+TEC3_pos', 
        'TEC3_pos+TEC4_pos', 
        'TEC4_pos+TEC5_pos', 
        'TEC5_pos+TEC6_pos', 
        'TEC6_pos+TEC7_pos', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_neg+TEC3_neg', 
        'TEC3_neg+TEC4_neg', 
        'TEC4_neg+TEC5_neg', 
        'TEC5_neg+TEC6_neg', 
        'TEC6_neg+TEC7_neg'
    )
)


process.tobTecStepSeedLayersPair = cms.EDProducer("SeedingLayersEDProducer",
    TEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        maxRing = cms.int32(5),
        minRing = cms.int32(5),
        skipClusters = cms.InputTag("tobTecStepClusters"),
        useRingSlector = cms.bool(True)
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters")
    ),
    layerList = cms.vstring(
        'TOB1+TEC1_pos', 
        'TOB1+TEC1_neg', 
        'TEC1_pos+TEC2_pos', 
        'TEC1_neg+TEC2_neg', 
        'TEC2_pos+TEC3_pos', 
        'TEC2_neg+TEC3_neg', 
        'TEC3_pos+TEC4_pos', 
        'TEC3_neg+TEC4_neg', 
        'TEC4_pos+TEC5_pos', 
        'TEC4_neg+TEC5_neg', 
        'TEC5_pos+TEC6_pos', 
        'TEC5_neg+TEC6_neg', 
        'TEC6_pos+TEC7_pos', 
        'TEC6_neg+TEC7_neg'
    )
)


process.tobTecStepSeedLayersTripl = cms.EDProducer("SeedingLayersEDProducer",
    MTEC = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        maxRing = cms.int32(7),
        minRing = cms.int32(6),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters"),
        useRingSlector = cms.bool(True)
    ),
    MTOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        rphiRecHits = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters")
    ),
    TOB = cms.PSet(
        TTRHBuilder = cms.string('WithTrackAngle'),
        clusterChargeCut = cms.PSet(
            refToPSet_ = cms.string('SiStripClusterChargeCutTight')
        ),
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        skipClusters = cms.InputTag("tobTecStepClusters")
    ),
    layerList = cms.vstring(
        'TOB1+TOB2+MTOB3', 
        'TOB1+TOB2+MTOB4', 
        'TOB1+TOB2+MTEC1_pos', 
        'TOB1+TOB2+MTEC1_neg'
    )
)


process.tobTecStepSeeds = cms.EDProducer("SeedCombiner",
    seedCollections = cms.VInputTag(cms.InputTag("tobTecStepSeedsTripl"), cms.InputTag("tobTecStepSeedsPair"))
)


process.tobTecStepSeedsPair = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
                ClusterShapeHitFilterName = cms.string('tobTecStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("tobTecStepHitDoubletsPair")
)


process.tobTecStepSeedsTripl = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('CombinedSeedComparitor'),
        comparitors = cms.VPSet(
            cms.PSet(
                ClusterShapeCacheSrc = cms.InputTag("siPixelClusterShapeCache"),
                ClusterShapeHitFilterName = cms.string('tobTecStepClusterShapeHitFilter'),
                ComponentName = cms.string('PixelClusterShapeSeedComparitor'),
                FilterAtHelixStage = cms.bool(True),
                FilterPixelHits = cms.bool(False),
                FilterStripHits = cms.bool(True)
            ), 
            cms.PSet(
                ComponentName = cms.string('StripSubClusterShapeSeedFilter'),
                FilterAtHelixStage = cms.bool(False),
                label = cms.untracked.string('Seeds'),
                maxNSat = cms.uint32(3),
                maxTrimmedSizeDiffNeg = cms.double(1.0),
                maxTrimmedSizeDiffPos = cms.double(0.7),
                seedCutMIPs = cms.double(0.35),
                seedCutSN = cms.double(7.0),
                subclusterCutMIPs = cms.double(0.45),
                subclusterCutSN = cms.double(12.0),
                subclusterWindow = cms.double(0.7),
                trimMaxADC = cms.double(30.0),
                trimMaxFracNeigh = cms.double(0.25),
                trimMaxFracTotal = cms.double(0.15)
            )
        ),
        mode = cms.string('and')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("tobTecStepHitTripletsTripl")
)


process.tobTecStepTrackCandidates = cms.EDProducer("CkfTrackCandidateMaker",
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    RedundantSeedCleaner = cms.string('CachingSeedCleanerBySharedInput'),
    SimpleMagneticField = cms.string(''),
    TrajectoryBuilder = cms.string('GroupedCkfTrajectoryBuilder'),
    TrajectoryBuilderPSet = cms.PSet(
        refToPSet_ = cms.string('tobTecStepTrajectoryBuilder')
    ),
    TrajectoryCleaner = cms.string('tobTecStepTrajectoryCleanerBySharedHits'),
    TransientInitialStateEstimatorParameters = cms.PSet(
        numberMeasurementsForFit = cms.int32(4),
        propagatorAlongTISE = cms.string('PropagatorWithMaterial'),
        propagatorOppositeTISE = cms.string('PropagatorWithMaterialOpposite')
    ),
    cleanTrajectoryAfterInOut = cms.bool(True),
    clustersToSkip = cms.InputTag("tobTecStepClusters"),
    doSeedingRegionRebuilding = cms.bool(True),
    maxNSeeds = cms.uint32(500000),
    maxSeedsBeforeCleaning = cms.uint32(5000),
    numHitsForSeedCleaner = cms.int32(50),
    onlyPixelHitsForSeedCleaner = cms.bool(True),
    reverseTrajectories = cms.bool(False),
    src = cms.InputTag("tobTecStepSeeds"),
    useHitsSplitting = cms.bool(True)
)


process.tobTecStepTrackingRegionsPair = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(0),
        originHalfLength = cms.double(30.0),
        originRadius = cms.double(6.0),
        precise = cms.bool(True),
        ptMin = cms.double(0.6),
        useMultipleScattering = cms.bool(False)
    )
)


process.tobTecStepTrackingRegionsTripl = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(0),
        originHalfLength = cms.double(20.0),
        originRadius = cms.double(3.5),
        precise = cms.bool(True),
        ptMin = cms.double(0.55),
        useMultipleScattering = cms.bool(False)
    )
)


process.tobTecStepTracks = cms.EDProducer("TrackProducer",
    AlgorithmName = cms.string('tobTecStep'),
    Fitter = cms.string('tobTecFlexibleKFFittingSmoother'),
    GeometricInnerState = cms.bool(False),
    MeasurementTracker = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag("MeasurementTrackerEvent"),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    SimpleMagneticField = cms.string(''),
    TTRHBuilder = cms.string('WithAngleAndTemplate'),
    TrajectoryInEvent = cms.bool(False),
    alias = cms.untracked.string('ctfWithMaterialTracks'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    clusterRemovalInfo = cms.InputTag(""),
    src = cms.InputTag("tobTecStepTrackCandidates"),
    useHitsSplitting = cms.bool(False),
    useSimpleMF = cms.bool(False)
)


process.topBottomClusterInfoProducer = cms.EDProducer("TopBottomClusterInfoProducer",
    pixelClustersNew = cms.InputTag("siPixelClustersTop"),
    pixelClustersOld = cms.InputTag("siPixelClusters"),
    pixelHitsNew = cms.InputTag("siPixelRecHitsTop"),
    pixelHitsOld = cms.InputTag("siPixelRecHits"),
    stripClustersNew = cms.InputTag("siStripClustersTop"),
    stripClustersOld = cms.InputTag("siStripClusters"),
    stripMonoHitsNew = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
    stripMonoHitsOld = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    stripStereoHitsNew = cms.InputTag("siStripMatchedRecHitsTop","stereoRecHit"),
    stripStereoHitsOld = cms.InputTag("siStripMatchedRecHits","stereoRecHit")
)


process.topBottomClusterInfoProducerBottom = cms.EDProducer("TopBottomClusterInfoProducer",
    pixelClustersNew = cms.InputTag("siPixelClustersBottom"),
    pixelClustersOld = cms.InputTag("siPixelClusters"),
    pixelHitsNew = cms.InputTag("siPixelRecHitsBottom"),
    pixelHitsOld = cms.InputTag("siPixelRecHits"),
    stripClustersNew = cms.InputTag("siStripClustersBottom"),
    stripClustersOld = cms.InputTag("siStripClusters"),
    stripMonoHitsNew = cms.InputTag("siStripMatchedRecHitsBottom","rphiRecHit"),
    stripMonoHitsOld = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    stripStereoHitsNew = cms.InputTag("siStripMatchedRecHitsBottom","stereoRecHit"),
    stripStereoHitsOld = cms.InputTag("siStripMatchedRecHits","stereoRecHit")
)


process.topBottomClusterInfoProducerTop = cms.EDProducer("TopBottomClusterInfoProducer",
    pixelClustersNew = cms.InputTag("siPixelClustersTop"),
    pixelClustersOld = cms.InputTag("siPixelClusters"),
    pixelHitsNew = cms.InputTag("siPixelRecHitsTop"),
    pixelHitsOld = cms.InputTag("siPixelRecHits"),
    stripClustersNew = cms.InputTag("siStripClustersTop"),
    stripClustersOld = cms.InputTag("siStripClusters"),
    stripMonoHitsNew = cms.InputTag("siStripMatchedRecHitsTop","rphiRecHit"),
    stripMonoHitsOld = cms.InputTag("siStripMatchedRecHits","rphiRecHit"),
    stripStereoHitsNew = cms.InputTag("siStripMatchedRecHitsTop","stereoRecHit"),
    stripStereoHitsOld = cms.InputTag("siStripMatchedRecHits","stereoRecHit")
)


process.trackClusterRemover = cms.EDProducer("TrackClusterRemover",
    TrackQuality = cms.string('highPurity'),
    maxChi2 = cms.double(30),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32(0),
    oldClusterRemovalInfo = cms.InputTag(""),
    overrideTrkQuals = cms.InputTag(""),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trackClassifier = cms.InputTag("","QualityMasks"),
    trajectories = cms.InputTag("")
)


process.trackExtrapolator = cms.EDProducer("TrackExtrapolator",
    trackQuality = cms.string('goodIterative'),
    trackSrc = cms.InputTag("generalTracks")
)


process.trackRefsForJets = cms.EDProducer("ChargedRefCandidateProducer",
    particleType = cms.string('pi+'),
    src = cms.InputTag("trackWithVertexRefSelector")
)


process.trackerClusterCheck = cms.EDProducer("ClusterCheckerEDProducer",
    ClusterCollectionLabel = cms.InputTag("siStripClusters"),
    MaxNumberOfCosmicClusters = cms.uint32(400000),
    MaxNumberOfPixelClusters = cms.uint32(40000),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClusters"),
    cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
    doClusterCheck = cms.bool(True),
    silentClusterCheck = cms.untracked.bool(False)
)


process.trackerClusterCheckPreSplitting = cms.EDProducer("ClusterCheckerEDProducer",
    ClusterCollectionLabel = cms.InputTag("siStripClusters"),
    MaxNumberOfCosmicClusters = cms.uint32(400000),
    MaxNumberOfPixelClusters = cms.uint32(40000),
    PixelClusterCollectionLabel = cms.InputTag("siPixelClustersPreSplitting"),
    cut = cms.string('strip < 400000 && pixel < 40000 && (strip < 50000 + 10*pixel) && (pixel < 5000 + 0.1*strip)'),
    doClusterCheck = cms.bool(True),
    silentClusterCheck = cms.untracked.bool(False)
)


process.tripletElectronClusterMask = cms.EDProducer("SeedClusterRemover",
    Common = cms.PSet(
        maxChi2 = cms.double(9.0)
    ),
    oldClusterRemovalInfo = cms.InputTag("pixelLessStepSeedClusterMask"),
    pixelClusters = cms.InputTag("siPixelClusters"),
    stripClusters = cms.InputTag("siStripClusters"),
    trajectories = cms.InputTag("tripletElectronSeeds")
)


process.tripletElectronHitDoublets = cms.EDProducer("HitPairEDProducer",
    clusterCheck = cms.InputTag("trackerClusterCheck"),
    layerPairs = cms.vuint32(0),
    maxElement = cms.uint32(50000000),
    maxElementTotal = cms.uint32(50000000),
    produceIntermediateHitDoublets = cms.bool(True),
    produceSeedingHitSets = cms.bool(False),
    seedingLayers = cms.InputTag("tripletElectronSeedLayers"),
    trackingRegions = cms.InputTag("tripletElectronTrackingRegions"),
    trackingRegionsSeedingLayers = cms.InputTag("")
)


process.tripletElectronHitTriplets = cms.EDProducer("PixelTripletHLTEDProducer",
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    doublets = cms.InputTag("tripletElectronHitDoublets"),
    extraHitRPhitolerance = cms.double(0.032),
    extraHitRZtolerance = cms.double(0.037),
    maxElement = cms.uint32(1000000),
    phiPreFiltering = cms.double(0.3),
    produceIntermediateHitTriplets = cms.bool(False),
    produceSeedingHitSets = cms.bool(True),
    useBending = cms.bool(True),
    useFixedPreFiltering = cms.bool(False),
    useMultScattering = cms.bool(True)
)


process.tripletElectronSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
    BPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
        skipClusters = cms.InputTag("pixelLessStepSeedClusterMask")
    ),
    FPix = cms.PSet(
        HitProducer = cms.string('siPixelRecHits'),
        TTRHBuilder = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
        skipClusters = cms.InputTag("pixelLessStepSeedClusterMask")
    ),
    layerList = cms.vstring(
        'BPix1+BPix2+BPix3', 
        'BPix1+BPix2+FPix1_pos', 
        'BPix1+BPix2+FPix1_neg', 
        'BPix1+FPix1_pos+FPix2_pos', 
        'BPix1+FPix1_neg+FPix2_neg'
    )
)


process.tripletElectronSeeds = cms.EDProducer("SeedCreatorFromRegionConsecutiveHitsEDProducer",
    MinOneOverPtError = cms.double(1),
    OriginTransverseErrorMultiplier = cms.double(1),
    SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none')
    ),
    SeedMomentumForBOFF = cms.double(5),
    TTRHBuilder = cms.string('WithTrackAngle'),
    forceKinematicWithRegionDirection = cms.bool(False),
    magneticField = cms.string('ParabolicMf'),
    propagator = cms.string('PropagatorWithMaterialParabolicMf'),
    seedingHitSets = cms.InputTag("tripletElectronHitTriplets")
)


process.tripletElectronTrackingRegions = cms.EDProducer("GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        nSigmaZ = cms.double(4),
        originHalfLength = cms.double(0),
        originRadius = cms.double(0.02),
        precise = cms.bool(True),
        ptMin = cms.double(1.0),
        useMultipleScattering = cms.bool(False)
    )
)


process.filterOutLowPt = cms.EDFilter("FilterOutLowPt",
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False),
    numtrack = cms.untracked.uint32(0),
    ptmin = cms.untracked.double(3),
    runControl = cms.untracked.bool(False),
    runControlNumber = cms.untracked.vuint32(319347),
    src = cms.untracked.InputTag("ALCARECOTkAlMinBias"),
    thresh = cms.untracked.int32(1)
)


process.firstStepGoodPrimaryVertices = cms.EDFilter("PrimaryVertexObjectFilter",
    filterParams = cms.PSet(
        maxRho = cms.double(2.0),
        maxZ = cms.double(15.0),
        minNdof = cms.double(25.0)
    ),
    src = cms.InputTag("firstStepPrimaryVertices")
)


process.jetsForCoreTracking = cms.EDFilter("CandPtrSelector",
    cut = cms.string('pt > 100 && abs(eta) < 2.5'),
    src = cms.InputTag("ak4CaloJetsForTrk")
)


process.jetsForCoreTrackingPreSplitting = cms.EDFilter("CandPtrSelector",
    cut = cms.string('pt > 100 && abs(eta) < 2.5'),
    src = cms.InputTag("ak4CaloJetsForTrkPreSplitting")
)


process.noscraping = cms.EDFilter("FilterOutScraping",
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False),
    numtrack = cms.untracked.uint32(10),
    src = cms.untracked.InputTag("ALCARECOTkAlMinBias"),
    thresh = cms.untracked.double(0.25)
)


process.primaryVertexFilter = cms.EDFilter("VertexSelector",
    cut = cms.string('!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2'),
    filter = cms.bool(True),
    src = cms.InputTag("offlinePrimaryVertices")
)


process.BeamSpotChecker = cms.EDAnalyzer("BeamSpotChecker",
    bsFromDB = cms.InputTag("myOfflineBeamSpot"),
    bsFromEvent = cms.InputTag("offlineBeamSpot"),
    errorThr = cms.double(3.402823466e+38),
    warningThr = cms.double(3.0)
)


process.PVValidation = cms.EDAnalyzer("PrimaryVertexValidation",
    Debug = cms.bool(False),
    TkClusParameters = cms.PSet(
        TkDAClusParameters = cms.PSet(
            Tmin = cms.double(2.0),
            Tpurge = cms.double(2.0),
            Tstop = cms.double(0.5),
            coolingFactor = cms.double(0.6),
            d0CutOff = cms.double(3.0),
            dzCutOff = cms.double(3.0),
            uniquetrkweight = cms.double(0.8),
            vertexSize = cms.double(0.006),
            zmerge = cms.double(0.01)
        ),
        algorithm = cms.string('DA_vect')
    ),
    TkFilterParameters = cms.PSet(
        algorithm = cms.string('filter'),
        maxD0Significance = cms.double(5.0),
        maxEta = cms.double(5.0),
        maxNormalizedChi2 = cms.double(5.0),
        minPixelLayersWithHits = cms.int32(2),
        minPt = cms.double(0.0),
        minSiliconLayersWithHits = cms.int32(5),
        trackQuality = cms.string('any')
    ),
    TrackCollectionTag = cms.InputTag("FinalTrackRefitter"),
    VertexCollectionTag = cms.InputTag("offlinePrimaryVertices"),
    askFirstLayerHit = cms.bool(False),
    doBPix = cms.untracked.bool(True),
    doFPix = cms.untracked.bool(True),
    forceBeamSpot = cms.untracked.bool(False),
    isLightNtuple = cms.bool(True),
    numberOfBins = cms.untracked.int32(48),
    probeEta = cms.untracked.double(2.5),
    probePt = cms.untracked.double(3.0),
    runControl = cms.untracked.bool(False),
    runControlNumber = cms.untracked.vuint32(319347),
    storeNtuple = cms.bool(False),
    useTracksFromRecoVtx = cms.bool(False)
)


process.DQMStore = cms.Service("DQMStore",
    LSbasedMode = cms.untracked.bool(False),
    collateHistograms = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(False),
    forceResetOnBeginLumi = cms.untracked.bool(False),
    referenceFileName = cms.untracked.string(''),
    saveByLumi = cms.untracked.bool(False),
    verbose = cms.untracked.int32(0),
    verboseQT = cms.untracked.int32(0)
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring(
        'FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'
    ),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1000)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring(
        'cout', 
        'cerr'
    ),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring(
        'cerr_stats', 
        'cout'
    ),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    CTPPSFastRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1357987)
    ),
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(987346)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(98765432)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6541321)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(654321)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(234567)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    fastSimProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(13579)
    ),
    fastTrackerRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(24680)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(88776655)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6453209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(54525)
    ),
    saveFileName = cms.untracked.string(''),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11223344)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('PrimaryVertexValidation_PVvalidation_StartGeom.root')
)


process.AnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('AnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum')
)


process.AnalyticalPropagatorParabolicMF = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('AnalyticalPropagatorParabolicMf'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf')
)


process.AnyDirectionAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('AnyDirectionAnalyticalPropagator'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('anyDirection')
)


process.BeamHaloMPropagatorAlong = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('BeamHaloMPropagatorAlong'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(10000),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(True)
)


process.BeamHaloMPropagatorOpposite = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('BeamHaloMPropagatorOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(10000),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(True)
)


process.BeamHaloPropagatorAlong = cms.ESProducer("BeamHaloPropagatorESProducer",
    ComponentName = cms.string('BeamHaloPropagatorAlong'),
    CrossingTrackerPropagator = cms.string('BeamHaloSHPropagatorAlong'),
    EndCapTrackerPropagator = cms.string('BeamHaloMPropagatorAlong'),
    PropagationDirection = cms.string('alongMomentum')
)


process.BeamHaloPropagatorAny = cms.ESProducer("BeamHaloPropagatorESProducer",
    ComponentName = cms.string('BeamHaloPropagatorAny'),
    CrossingTrackerPropagator = cms.string('BeamHaloSHPropagatorAny'),
    EndCapTrackerPropagator = cms.string('BeamHaloMPropagatorAlong'),
    PropagationDirection = cms.string('anyDirection')
)


process.BeamHaloPropagatorOpposite = cms.ESProducer("BeamHaloPropagatorESProducer",
    ComponentName = cms.string('BeamHaloPropagatorOpposite'),
    CrossingTrackerPropagator = cms.string('BeamHaloSHPropagatorOpposite'),
    EndCapTrackerPropagator = cms.string('BeamHaloMPropagatorOpposite'),
    PropagationDirection = cms.string('oppositeToMomentum')
)


process.BeamHaloSHPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('BeamHaloSHPropagatorAlong'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.BeamHaloSHPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('BeamHaloSHPropagatorAny'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.BeamHaloSHPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('BeamHaloSHPropagatorOpposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.Chi2MeasurementEstimator = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('Chi2'),
    MaxChi2 = cms.double(30),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3)
)


process.Chi2MeasurementEstimatorForP5 = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('Chi2MeasurementEstimatorForP5'),
    MaxChi2 = cms.double(100.0),
    MaxDisplacement = cms.double(100),
    MaxSagitta = cms.double(-1),
    MinPtForHitRecoveryInGluedDet = cms.double(100000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(4.0)
)


process.ClusterShapeHitFilterESProducer = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('ClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase0.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase0.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutNone')
    )
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.DummyDetLayerGeometry = cms.ESProducer("DetLayerGeometryESProducer",
    ComponentName = cms.string('DummyDetLayerGeometry')
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.FittingSmootherRKP5 = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('FittingSmootherRKP5'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('RKFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(4),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('RKSmoother'),
    appendToDataLabel = cms.string('')
)


process.FlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('FlexibleKFFittingSmoother'),
    appendToDataLabel = cms.string(''),
    looperFitter = cms.string('LooperFittingSmoother'),
    standardFitter = cms.string('KFFittingSmootherWithOutliersRejectionAndRK')
)


process.GlobalDetLayerGeometry = cms.ESProducer("GlobalDetLayerGeometryESProducer",
    ComponentName = cms.string('GlobalDetLayerGeometry')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.KFFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('KFFittingSmoother'),
    EstimateCut = cms.double(-1),
    Fitter = cms.string('KFFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('KFSmoother'),
    appendToDataLabel = cms.string('')
)


process.KFFittingSmootherBeamHalo = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('KFFittingSmootherBH'),
    EstimateCut = cms.double(-1),
    Fitter = cms.string('KFFitterBH'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('KFSmootherBH'),
    appendToDataLabel = cms.string('')
)


process.KFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('KFFittingSmootherWithOutliersRejectionAndRK'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('RKFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('RKSmoother'),
    appendToDataLabel = cms.string('')
)


process.KFSwitching1DUpdatorESProducer = cms.ESProducer("KFSwitching1DUpdatorESProducer",
    ComponentName = cms.string('KFSwitching1DUpdator'),
    doEndCap = cms.bool(False)
)


process.KFTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('KFFitter'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('PropagatorWithMaterial'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.KFTrajectoryFitterBeamHalo = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('KFFitterBH'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('BeamHaloPropagatorAlong'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.KFTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('KFSmoother'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('PropagatorWithMaterial'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100),
    minHits = cms.int32(3)
)


process.KFTrajectorySmootherBeamHalo = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('KFSmootherBH'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('BeamHaloPropagatorAlong'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100),
    minHits = cms.int32(3)
)


process.KFUpdatorESProducer = cms.ESProducer("KFUpdatorESProducer",
    ComponentName = cms.string('KFUpdator')
)


process.LooperFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('LooperFittingSmoother'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('LooperFitter'),
    LogPixelProbabilityCut = cms.double(-14.0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('LooperSmoother'),
    appendToDataLabel = cms.string('')
)


process.LooperTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('LooperFitter'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.LooperTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('LooperSmoother'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.MRHChi2MeasurementEstimator = cms.ESProducer("MRHChi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('MRHChi2'),
    MaxChi2 = cms.double(30.0),
    nSigma = cms.double(3.0)
)


process.MRHFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('MRHFittingSmoother'),
    EstimateCut = cms.double(-1),
    Fitter = cms.string('MRHFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('MRHSmoother'),
    appendToDataLabel = cms.string('')
)


process.MRHTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('MRHFitter'),
    Estimator = cms.string('MRHChi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.MRHTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('MRHSmoother'),
    Estimator = cms.string('MRHChi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100),
    minHits = cms.int32(3)
)


process.MaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterial'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMf'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.MeasurementTracker = cms.ESProducer("MeasurementTrackerESProducer",
    ComponentName = cms.string(''),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    MaskBadAPVFibers = cms.bool(True),
    PixelCPE = cms.string('PixelCPEGeneric'),
    SiStripQualityLabel = cms.string(''),
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    UsePixelModuleQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    UseStripAPVFiberQualityDB = cms.bool(True),
    UseStripModuleQualityDB = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    badStripCuts = cms.PSet(
        TEC = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TIB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TID = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TOB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        )
    )
)


process.MeasurementTrackerBottom = cms.ESProducer("MeasurementTrackerESProducer",
    ComponentName = cms.string('MeasurementTrackerBottom'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    MaskBadAPVFibers = cms.bool(True),
    PixelCPE = cms.string('PixelCPEGeneric'),
    SiStripQualityLabel = cms.string(''),
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    UsePixelModuleQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    UseStripAPVFiberQualityDB = cms.bool(True),
    UseStripModuleQualityDB = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    badStripCuts = cms.PSet(
        TEC = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TIB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TID = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TOB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        )
    ),
    pixelClusterProducer = cms.string('siPixelClustersBottom'),
    stripClusterProducer = cms.string('siStripClustersBottom')
)


process.MeasurementTrackerTop = cms.ESProducer("MeasurementTrackerESProducer",
    ComponentName = cms.string('MeasurementTrackerTop'),
    DebugPixelModuleQualityDB = cms.untracked.bool(False),
    DebugPixelROCQualityDB = cms.untracked.bool(False),
    DebugStripAPVFiberQualityDB = cms.untracked.bool(False),
    DebugStripModuleQualityDB = cms.untracked.bool(False),
    DebugStripStripQualityDB = cms.untracked.bool(False),
    HitMatcher = cms.string('StandardMatcher'),
    MaskBadAPVFibers = cms.bool(True),
    PixelCPE = cms.string('PixelCPEGeneric'),
    SiStripQualityLabel = cms.string(''),
    StripCPE = cms.string('StripCPEfromTrackAngle'),
    UsePixelModuleQualityDB = cms.bool(True),
    UsePixelROCQualityDB = cms.bool(True),
    UseStripAPVFiberQualityDB = cms.bool(True),
    UseStripModuleQualityDB = cms.bool(True),
    UseStripStripQualityDB = cms.bool(True),
    badStripCuts = cms.PSet(
        TEC = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TIB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TID = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        ),
        TOB = cms.PSet(
            maxBad = cms.uint32(4),
            maxConsecutiveBad = cms.uint32(2)
        )
    ),
    pixelClusterProducer = cms.string('siPixelClustersTop'),
    stripClusterProducer = cms.string('siStripClustersTop')
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")


process.OppositeAnalyticalPropagator = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('AnalyticalPropagatorOpposite'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum')
)


process.OppositeAnalyticalPropagatorParabolicMF = cms.ESProducer("AnalyticalPropagatorESProducer",
    ComponentName = cms.string('AnalyticalPropagatorParabolicMfOpposite'),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf')
)


process.OppositeMaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.OppositeMaterialPropagatorParabolicMF = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string('ParabolicMf'),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(False)
)


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.PixelCPEGenericESProducer = cms.ESProducer("PixelCPEGenericESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('PixelCPEGeneric'),
    DoCosmics = cms.bool(False),
    EdgeClusterErrorX = cms.double(50.0),
    EdgeClusterErrorY = cms.double(85.0),
    IrradiationBiasCorrection = cms.bool(False),
    LoadTemplatesFromDB = cms.bool(True),
    MagneticFieldRecord = cms.ESInputTag(""),
    PixelErrorParametrization = cms.string('NOTcmsim'),
    TruncatePixelCharge = cms.bool(True),
    UseErrorsFromTemplates = cms.bool(True),
    eff_charge_cut_highX = cms.double(1.0),
    eff_charge_cut_highY = cms.double(1.0),
    eff_charge_cut_lowX = cms.double(0.0),
    eff_charge_cut_lowY = cms.double(0.0),
    inflate_all_errors_no_trk_angle = cms.bool(False),
    inflate_errors = cms.bool(False),
    size_cutX = cms.double(3.0),
    size_cutY = cms.double(3.0),
    useLAAlignmentOffsets = cms.bool(False),
    useLAWidthFromDB = cms.bool(True)
)


process.PropagatorWithMaterialForLoopers = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForLoopers'),
    Mass = cms.double(0.1396),
    MaxDPhi = cms.double(4.0),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1),
    useOldAnalPropLogic = cms.bool(False),
    useRungeKutta = cms.bool(False)
)


process.PropagatorWithMaterialForLoopersOpposite = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('PropagatorWithMaterialForLoopersOpposite'),
    Mass = cms.double(0.1396),
    MaxDPhi = cms.double(4.0),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1),
    useOldAnalPropLogic = cms.bool(False),
    useRungeKutta = cms.bool(False)
)


process.RK1DFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('RK1DFittingSmoother'),
    EstimateCut = cms.double(-1),
    Fitter = cms.string('RK1DFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('RK1DSmoother'),
    appendToDataLabel = cms.string('')
)


process.RK1DTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('RK1DFitter'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFSwitching1DUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.RK1DTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('RK1DSmoother'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFSwitching1DUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100),
    minHits = cms.int32(3)
)


process.RKFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('RKFittingSmoother'),
    EstimateCut = cms.double(-1),
    Fitter = cms.string('RKFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(5),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('RKSmoother'),
    appendToDataLabel = cms.string('')
)


process.RKOutliers1DFittingSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('RKOutliers1DFittingSmoother'),
    EstimateCut = cms.double(20.0),
    Fitter = cms.string('RK1DFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('RK1DSmoother'),
    appendToDataLabel = cms.string('')
)


process.RKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('RKFitter'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(3)
)


process.RKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('RKSmoother'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(100),
    minHits = cms.int32(3)
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.RungeKuttaTrackerPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('RungeKuttaTrackerPropagator'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(-1.0),
    useRungeKutta = cms.bool(True)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.SteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAlong'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.SteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAny'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('anyDirection'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.SteppingHelixPropagatorOpposite = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorOpposite'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.StripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('SimpleStripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TTRHBuilderAngleAndTemplate = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('WithAngleAndTemplate'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('PixelCPETemplateReco'),
    StripCPE = cms.string('StripCPEfromTrackAngle')
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.XMLFromDBSource = cms.ESProducer("XMLIdealGeometryESProducer",
    label = cms.string('Extended'),
    rootDDName = cms.string('cms:OCMS')
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.beamHaloNavigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('BeamHaloNavigationSchool'),
    SimpleMagneticField = cms.string('')
)


process.conv2StepFitterSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('conv2StepFitterSmoother'),
    EstimateCut = cms.double(30),
    Fitter = cms.string('RKFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('conv2StepRKSmoother'),
    appendToDataLabel = cms.string('')
)


process.conv2StepRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('conv2StepRKSmoother'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.convStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('convStepChi2Est'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(100),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1)
)


process.convStepFitterSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('convStepFitterSmoother'),
    EstimateCut = cms.double(30),
    Fitter = cms.string('RKFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('convStepRKSmoother'),
    appendToDataLabel = cms.string('')
)


process.convStepRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('convStepRKSmoother'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(3)
)


process.cosmicsNavigationSchoolESProducer = cms.ESProducer("SkippingLayerCosmicNavigationSchoolESProducer",
    ComponentName = cms.string('CosmicNavigationSchool'),
    allSelf = cms.bool(True),
    noPXB = cms.bool(False),
    noPXF = cms.bool(False),
    noTEC = cms.bool(False),
    noTIB = cms.bool(False),
    noTID = cms.bool(False),
    noTOB = cms.bool(False),
    selfSearch = cms.bool(True)
)


process.detachedQuadStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('detachedQuadStepChi2Est'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3),
    pTChargeCutThreshold = cms.double(-1)
)


process.detachedQuadStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('detachedQuadStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.detachedTripletStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('detachedTripletStepChi2Est'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1)
)


process.detachedTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('detachedTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.13)
)


process.duplicateTrackCandidatesChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('duplicateTrackCandidatesChi2Est'),
    MaxChi2 = cms.double(100),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.highPtTripletStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('highPtTripletStepChi2Est'),
    MaxChi2 = cms.double(30),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3),
    pTChargeCutThreshold = cms.double(15.0)
)


process.highPtTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('highPtTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.hitCollectorForCosmicDCSeeds = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hitCollectorForCosmicDCSeeds'),
    MaxChi2 = cms.double(100.0),
    MaxDisplacement = cms.double(100),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(4.0)
)


process.hitCollectorForOutInMuonSeeds = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('hitCollectorForOutInMuonSeeds'),
    MaxChi2 = cms.double(100.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(4.0)
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.initialStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('initialStepChi2Est'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.initialStepChi2EstPreSplitting = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('initialStepChi2EstPreSplitting'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1)
)


process.jetCoreRegionalStepChi2Est = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('jetCoreRegionalStepChi2Est'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.lowPtQuadStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('lowPtQuadStepChi2Est'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3),
    pTChargeCutThreshold = cms.double(-1)
)


process.lowPtQuadStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('lowPtQuadStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.lowPtTripletStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('lowPtTripletStepChi2Est'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1)
)


process.lowPtTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('lowPtTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.16)
)


process.mixedTripletStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('mixedTripletStepChi2Est'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1)
)


process.mixedTripletStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('mixedTripletStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase0.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase0.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    )
)


process.mixedTripletStepPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('mixedTripletStepPropagator'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(0.1),
    useRungeKutta = cms.bool(False)
)


process.mixedTripletStepPropagatorOpposite = cms.ESProducer("PropagatorWithMaterialESProducer",
    ComponentName = cms.string('mixedTripletStepPropagatorOpposite'),
    Mass = cms.double(0.105),
    MaxDPhi = cms.double(1.6),
    PropagationDirection = cms.string('oppositeToMomentum'),
    SimpleMagneticField = cms.string(''),
    ptMin = cms.double(0.1),
    useRungeKutta = cms.bool(False)
)


process.mixedTripletStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('mixedTripletStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.muonSeededFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(False),
    ComponentName = cms.string('muonSeededFittingSmootherWithOutliersRejectionAndRK'),
    EstimateCut = cms.double(50.0),
    Fitter = cms.string('RKFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(3),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('RKSmoother'),
    appendToDataLabel = cms.string('')
)


process.muonSeededMeasurementEstimatorForInOut = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('muonSeededMeasurementEstimatorForInOut'),
    MaxChi2 = cms.double(80.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(4.0)
)


process.muonSeededMeasurementEstimatorForOutIn = cms.ESProducer("Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string('muonSeededMeasurementEstimatorForOutIn'),
    MaxChi2 = cms.double(30.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(-1.0),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    nSigma = cms.double(3.0)
)


process.muonSeededTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('muonSeededTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(1.0),
    ValidHitBonus = cms.double(1000.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.1)
)


process.myTTRHBuilderWithoutAngle4MixedPairs = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('TTRHBuilderWithoutAngle4MixedPairs'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('PixelCPEGeneric'),
    StripCPE = cms.string('Fake')
)


process.myTTRHBuilderWithoutAngle4MixedTriplets = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('TTRHBuilderWithoutAngle4MixedTriplets'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('PixelCPEGeneric'),
    StripCPE = cms.string('Fake')
)


process.myTTRHBuilderWithoutAngle4PixelPairs = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('TTRHBuilderWithoutAngle4PixelPairs'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('PixelCPEGeneric'),
    StripCPE = cms.string('Fake')
)


process.myTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('TTRHBuilderWithoutAngle4PixelTriplets'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('PixelCPEGeneric'),
    StripCPE = cms.string('Fake')
)


process.navigationSchoolESProducer = cms.ESProducer("NavigationSchoolESProducer",
    ComponentName = cms.string('SimpleNavigationSchool'),
    SimpleMagneticField = cms.string('')
)


process.pixelLessStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('pixelLessStepChi2Est'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1)
)


process.pixelLessStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('pixelLessStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase0.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase0.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    ),
    doStripShapeCut = cms.bool(False)
)


process.pixelLessStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('pixelLessStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.11)
)


process.pixelPairStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('pixelPairStepChi2Est'),
    MaxChi2 = cms.double(9.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutLoose')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(15.0)
)


process.pixelPairStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('pixelPairStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.095)
)


process.siPixel2DTemplateDBObjectESProducer = cms.ESProducer("SiPixel2DTemplateDBObjectESProducer")


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    ),
    siPixelQualityLabel = cms.string('')
)


process.siPixelTemplateDBObjectESProducer = cms.ESProducer("SiPixelTemplateDBObjectESProducer")


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.templates = cms.ESProducer("PixelCPETemplateRecoESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('PixelCPETemplateReco'),
    DoCosmics = cms.bool(False),
    DoLorentz = cms.bool(True),
    LoadTemplatesFromDB = cms.bool(True),
    UseClusterSplitter = cms.bool(False),
    speed = cms.int32(-2)
)


process.templates2 = cms.ESProducer("PixelCPEClusterRepairESProducer",
    Alpha2Order = cms.bool(True),
    ClusterProbComputationFlag = cms.int32(0),
    ComponentName = cms.string('PixelCPEClusterRepair'),
    DoCosmics = cms.bool(False),
    DoLorentz = cms.bool(True),
    LoadTemplatesFromDB = cms.bool(True),
    MaxSizeMismatchInY = cms.double(0.3),
    MinChargeRatio = cms.double(0.8),
    Recommend2D = cms.vstring(
        'PXB 2', 
        'PXB 3', 
        'PXB 4'
    ),
    RunDamagedClusters = cms.bool(False),
    UseClusterSplitter = cms.bool(False),
    speed = cms.int32(-2)
)


process.tobTecFlexibleKFFittingSmoother = cms.ESProducer("FlexibleKFFittingSmootherESProducer",
    ComponentName = cms.string('tobTecFlexibleKFFittingSmoother'),
    appendToDataLabel = cms.string(''),
    looperFitter = cms.string('tobTecStepFitterSmootherForLoopers'),
    standardFitter = cms.string('tobTecStepFitterSmoother')
)


process.tobTecStepChi2Est = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
    ComponentName = cms.string('tobTecStepChi2Est'),
    MaxChi2 = cms.double(16.0),
    MaxDisplacement = cms.double(0.5),
    MaxSagitta = cms.double(2),
    MinPtForHitRecoveryInGluedDet = cms.double(1000000000000),
    MinimalTolerance = cms.double(0.5),
    appendToDataLabel = cms.string(''),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    ),
    nSigma = cms.double(3.0),
    pTChargeCutThreshold = cms.double(-1)
)


process.tobTecStepClusterShapeHitFilter = cms.ESProducer("ClusterShapeHitFilterESProducer",
    ComponentName = cms.string('tobTecStepClusterShapeHitFilter'),
    PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase0.par'),
    PixelShapeFileL1 = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShapePhase0.par'),
    clusterChargeCut = cms.PSet(
        refToPSet_ = cms.string('SiStripClusterChargeCutTight')
    ),
    doStripShapeCut = cms.bool(False)
)


process.tobTecStepFitterSmoother = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('tobTecStepFitterSmoother'),
    EstimateCut = cms.double(30),
    Fitter = cms.string('tobTecStepRKFitter'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(7),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('tobTecStepRKSmoother'),
    appendToDataLabel = cms.string('')
)


process.tobTecStepFitterSmootherForLoopers = cms.ESProducer("KFFittingSmootherESProducer",
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('tobTecStepFitterSmootherForLoopers'),
    EstimateCut = cms.double(30),
    Fitter = cms.string('tobTecStepRKFitterForLoopers'),
    LogPixelProbabilityCut = cms.double(0),
    MaxFractionOutliers = cms.double(0.3),
    MaxNumberOfOutliers = cms.int32(3),
    MinDof = cms.int32(2),
    MinNumberOfHits = cms.int32(7),
    NoInvalidHitsBeginEnd = cms.bool(True),
    NoOutliersBeginEnd = cms.bool(False),
    RejectTracks = cms.bool(True),
    Smoother = cms.string('tobTecStepRKSmootherForLoopers'),
    appendToDataLabel = cms.string('')
)


process.tobTecStepRKTrajectoryFitter = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('tobTecStepRKFitter'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(7)
)


process.tobTecStepRKTrajectoryFitterForLoopers = cms.ESProducer("KFTrajectoryFitterESProducer",
    ComponentName = cms.string('tobTecStepRKFitterForLoopers'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    minHits = cms.int32(7)
)


process.tobTecStepRKTrajectorySmoother = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('tobTecStepRKSmoother'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('RungeKuttaTrackerPropagator'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(7)
)


process.tobTecStepRKTrajectorySmootherForLoopers = cms.ESProducer("KFTrajectorySmootherESProducer",
    ComponentName = cms.string('tobTecStepRKSmootherForLoopers'),
    Estimator = cms.string('Chi2'),
    Propagator = cms.string('PropagatorWithMaterialForLoopers'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    Updator = cms.string('KFUpdator'),
    appendToDataLabel = cms.string(''),
    errorRescaling = cms.double(10.0),
    minHits = cms.int32(7)
)


process.tobTecStepTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('tobTecStepTrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.09)
)


process.trackAlgoPriorityOrder = cms.ESProducer("TrackAlgoPriorityOrderESProducer",
    ComponentName = cms.string('trackAlgoPriorityOrder'),
    algoOrder = cms.vstring(
        'initialStep', 
        'detachedTripletStep', 
        'lowPtTripletStep', 
        'pixelPairStep', 
        'mixedTripletStep', 
        'pixelLessStep', 
        'tobTecStep', 
        'jetCoreRegionalStep', 
        'muonSeededStepInOut', 
        'muonSeededStepOutIn'
    ),
    appendToDataLabel = cms.string('')
)


process.trackSelectionLwtnn = cms.ESProducer("LwtnnESProducer",
    ComponentName = cms.string('trackSelectionLwtnn'),
    appendToDataLabel = cms.string(''),
    fileName = cms.FileInPath('RecoTracker/FinalTrackSelectors/data/LWTNN_network_10_5_X_v1.json')
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.trajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
    ComponentName = cms.string('TrajectoryCleanerBySharedHits'),
    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
    MissingHitPenalty = cms.double(20.0),
    ValidHitBonus = cms.double(5.0),
    allowSharedFirstHit = cms.bool(True),
    fractionShared = cms.double(0.19)
)


process.ttrhbwor = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('WithoutRefit'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('Fake'),
    PixelCPE = cms.string('Fake'),
    StripCPE = cms.string('Fake')
)


process.ttrhbwr = cms.ESProducer("TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string('WithTrackAngle'),
    ComputeCoarseLocalPositionFromDisk = cms.bool(False),
    Matcher = cms.string('StandardMatcher'),
    PixelCPE = cms.string('PixelCPEGeneric'),
    StripCPE = cms.string('StripCPEfromTrackAngle')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('102X_dataRun2_Prompt_v7'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ), 
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ), 
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(False),
    useHFUpgrade = cms.bool(False),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(True),
    useLayer0Weight = cms.bool(False)
)


process.prefer("es_hardcode")

process.InitialStepPreSplittingTask = cms.Task(process.MeasurementTrackerEvent, process.ak4CaloJetsForTrkPreSplitting, process.caloTowerForTrkPreSplitting, process.firstStepPrimaryVerticesPreSplitting, process.initialStepHitDoubletsPreSplitting, process.initialStepHitTripletsPreSplitting, process.initialStepSeedLayersPreSplitting, process.initialStepSeedsPreSplitting, process.initialStepTrackCandidatesPreSplitting, process.initialStepTrackRefsForJetsPreSplitting, process.initialStepTrackingRegionsPreSplitting, process.initialStepTracksPreSplitting, process.jetsForCoreTrackingPreSplitting, process.siPixelClusterShapeCache, process.siPixelClusters, process.siPixelRecHits, process.trackerClusterCheckPreSplitting)


process.muonSeededStepDebugInOutTask = cms.Task(process.muonSeededSeedsInOutAsTracks, process.muonSeededTrackCandidatesInOutAsTracks)


process.doAlldEdXEstimatorsTask = cms.Task(process.dedxHarmonic2, process.dedxHitInfo, process.dedxPixelAndStripHarmonic2T085, process.dedxPixelHarmonic2, process.dedxTruncated40)


process.caloJetsForTrkTask = cms.Task(process.ak4CaloJetsForTrk, process.caloTowerForTrk)


process.LowPtQuadStepTask = cms.Task(process.lowPtQuadStep, process.lowPtQuadStepClusters, process.lowPtQuadStepHitDoublets, process.lowPtQuadStepHitQuadruplets, process.lowPtQuadStepSeedLayers, process.lowPtQuadStepSeeds, process.lowPtQuadStepTrackCandidates, process.lowPtQuadStepTrackingRegions, process.lowPtQuadStepTracks)


process.ConvStepTask = cms.Task(process.convClusters, process.convLayerPairs, process.convStepSelector, process.convStepTracks, process.convTrackCandidates, process.photonConvTrajSeedFromSingleLeg)


process.HighPtTripletStepTask = cms.Task(process.highPtTripletStep, process.highPtTripletStepClusters, process.highPtTripletStepHitDoublets, process.highPtTripletStepHitTriplets, process.highPtTripletStepSeedLayers, process.highPtTripletStepSeeds, process.highPtTripletStepTrackCandidates, process.highPtTripletStepTrackingRegions, process.highPtTripletStepTracks)


process.Conv2StepTask = cms.Task(process.conv2Clusters, process.conv2LayerPairs, process.conv2StepSelector, process.conv2StepTracks, process.conv2TrackCandidates, process.photonConvTrajSeedFromQuadruplets)


process.MixedTripletStepTask = cms.Task(process.chargeCut2069Clusters, process.mixedTripletStep, process.mixedTripletStepClassifier1, process.mixedTripletStepClassifier2, process.mixedTripletStepClusters, process.mixedTripletStepHitDoubletsA, process.mixedTripletStepHitDoubletsB, process.mixedTripletStepHitTripletsA, process.mixedTripletStepHitTripletsB, process.mixedTripletStepSeedLayersA, process.mixedTripletStepSeedLayersB, process.mixedTripletStepSeeds, process.mixedTripletStepSeedsA, process.mixedTripletStepSeedsB, process.mixedTripletStepTrackCandidates, process.mixedTripletStepTrackingRegionsA, process.mixedTripletStepTrackingRegionsB, process.mixedTripletStepTracks)


process.DetachedTripletStepTask = cms.Task(process.detachedTripletStep, process.detachedTripletStepClassifier1, process.detachedTripletStepClassifier2, process.detachedTripletStepClusters, process.detachedTripletStepHitDoublets, process.detachedTripletStepHitTriplets, process.detachedTripletStepSeedLayers, process.detachedTripletStepSeeds, process.detachedTripletStepTrackCandidates, process.detachedTripletStepTrackingRegions, process.detachedTripletStepTracks)


process.JetCoreRegionalStepTask = cms.Task(process.firstStepGoodPrimaryVertices, process.jetCoreRegionalStep, process.jetCoreRegionalStepHitDoublets, process.jetCoreRegionalStepSeedLayers, process.jetCoreRegionalStepSeeds, process.jetCoreRegionalStepTrackCandidates, process.jetCoreRegionalStepTrackingRegions, process.jetCoreRegionalStepTracks, process.jetsForCoreTracking)


process.DetachedQuadStepTask = cms.Task(process.detachedQuadStep, process.detachedQuadStepClusters, process.detachedQuadStepHitDoublets, process.detachedQuadStepHitQuadruplets, process.detachedQuadStepSeedLayers, process.detachedQuadStepSeeds, process.detachedQuadStepTrackCandidates, process.detachedQuadStepTrackingRegions, process.detachedQuadStepTracks)


process.muonSeededStepCoreInOutTask = cms.Task(process.muonSeededSeedsInOut, process.muonSeededTrackCandidatesInOut, process.muonSeededTracksInOut)


process.TobTecStepTask = cms.Task(process.tobTecStep, process.tobTecStepClassifier1, process.tobTecStepClassifier2, process.tobTecStepClusters, process.tobTecStepHitDoubletsPair, process.tobTecStepHitDoubletsTripl, process.tobTecStepHitTripletsTripl, process.tobTecStepSeedLayersPair, process.tobTecStepSeedLayersTripl, process.tobTecStepSeeds, process.tobTecStepSeedsPair, process.tobTecStepSeedsTripl, process.tobTecStepTrackCandidates, process.tobTecStepTrackingRegionsPair, process.tobTecStepTrackingRegionsTripl, process.tobTecStepTracks)


process.muonSeededStepCoreOutInTask = cms.Task(process.muonSeededSeedsOutIn, process.muonSeededTrackCandidatesOutIn, process.muonSeededTracksOutIn)


process.cosmicDCTracksSeqTask = cms.Task(process.cosmicDCCkfTrackCandidates, process.cosmicDCSeeds, process.cosmicDCTracks)


process.PixelLessStepTask = cms.Task(process.pixelLessStep, process.pixelLessStepClassifier1, process.pixelLessStepClassifier2, process.pixelLessStepClusters, process.pixelLessStepHitDoublets, process.pixelLessStepHitTriplets, process.pixelLessStepSeedLayers, process.pixelLessStepSeeds, process.pixelLessStepTrackCandidates, process.pixelLessStepTrackingRegions, process.pixelLessStepTracks)


process.PixelPairStepTask = cms.Task(process.pixelPairStep, process.pixelPairStepClusters, process.pixelPairStepHitDoublets, process.pixelPairStepSeedLayers, process.pixelPairStepSeeds, process.pixelPairStepTrackCandidates, process.pixelPairStepTrackingRegions, process.pixelPairStepTracks)


process.muonSeededStepExtraInOutTask = cms.Task(process.muonSeededTracksInOutClassifier)


process.LowPtTripletStepTask = cms.Task(process.lowPtTripletStep, process.lowPtTripletStepClusters, process.lowPtTripletStepHitDoublets, process.lowPtTripletStepHitTriplets, process.lowPtTripletStepSeedLayers, process.lowPtTripletStepSeeds, process.lowPtTripletStepTrackCandidates, process.lowPtTripletStepTrackingRegions, process.lowPtTripletStepTracks)


process.InitialStepTask = cms.Task(process.caloJetsForTrkTask, process.firstStepPrimaryVertices, process.firstStepPrimaryVerticesUnsorted, process.initialStep, process.initialStepClassifier1, process.initialStepClassifier2, process.initialStepClassifier3, process.initialStepHitDoublets, process.initialStepHitTriplets, process.initialStepSeedLayers, process.initialStepSeeds, process.initialStepTrackCandidates, process.initialStepTrackRefsForJets, process.initialStepTrackingRegions, process.initialStepTracks)


process.generalTracksTask = cms.Task(process.duplicateTrackCandidates, process.duplicateTrackClassifier, process.generalTracks, process.mergedDuplicateTracks)


process.electronSeedsSeqTask = cms.Task(process.initialStepSeedClusterMask, process.mixedTripletStepSeedClusterMask, process.newCombinedSeeds, process.pixelLessStepSeedClusterMask, process.pixelPairElectronHitDoublets, process.pixelPairElectronSeedLayers, process.pixelPairElectronSeeds, process.pixelPairElectronTrackingRegions, process.pixelPairStepSeedClusterMask, process.stripPairElectronHitDoublets, process.stripPairElectronSeedLayers, process.stripPairElectronSeeds, process.stripPairElectronTrackingRegions, process.tripletElectronClusterMask, process.tripletElectronHitDoublets, process.tripletElectronHitTriplets, process.tripletElectronSeedLayers, process.tripletElectronSeeds, process.tripletElectronTrackingRegions)


process.muonSeededStepExtraTask = cms.Task(process.muonSeededStepExtraInOutTask, process.muonSeededTracksOutInClassifier)


process.muonSeededStepDebugTask = cms.Task(process.muonSeededSeedsOutInAsTracks, process.muonSeededStepDebugInOutTask, process.muonSeededTrackCandidatesOutInAsTracks)


process.iterTrackingEarlyTask = cms.Task(process.DetachedTripletStepTask, process.InitialStepTask, process.JetCoreRegionalStepTask, process.LowPtTripletStepTask, process.MixedTripletStepTask, process.PixelLessStepTask, process.PixelPairStepTask, process.TobTecStepTask)


process.muonSeededStepCoreTask = cms.Task(process.muonSeededStepCoreInOutTask, process.muonSeededStepCoreOutInTask)


process.muonSeededStepTask = cms.Task(process.earlyMuons, process.muonSeededStepCoreTask, process.muonSeededStepExtraTask)


process.iterTrackingTask = cms.Task(process.ConvStepTask, process.InitialStepPreSplittingTask, process.conversionStepTracks, process.earlyGeneralTracks, process.generalTracksTask, process.iterTrackingEarlyTask, process.muonSeededStepTask, process.preDuplicateMergingGeneralTracks, process.trackerClusterCheck)


process.regionalCosmicTracksSeq = cms.Sequence(process.regionalCosmicTrackerSeedingLayers+process.regionalCosmicTrackerSeeds+process.regionalCosmicCkfTrackCandidates+process.regionalCosmicTracks)


process.doAlldEdXEstimatorsCTF = cms.Sequence(process.dedxTruncated40CTF+process.dedxHitInfoCTF+process.dedxHarmonic2CTF)


process.LowPtQuadStep = cms.Sequence(process.LowPtQuadStepTask)


process.electronSeedsSeq = cms.Sequence(process.electronSeedsSeqTask)


process.HighPtTripletStep = cms.Sequence(process.HighPtTripletStepTask)


process.muonSeededStepCore = cms.Sequence(process.muonSeededStepCoreTask)


process.ctfTracksCombinedSeeds = cms.Sequence(process.MixedLayerPairs+process.globalSeedsFromPairsWithVertices+process.PixelLayerTriplets+process.globalSeedsFromTriplets+process.globalCombinedSeeds+process.ckfTrackCandidatesCombinedSeeds+process.ctfCombinedSeeds)


process.cosmictracksP5Top = cms.Sequence(process.cosmicseedfinderP5Top+process.cosmicCandidateFinderP5Top+process.cosmictrackfinderP5Top)


process.Conv2Step = cms.Sequence(process.Conv2StepTask)


process.PixelLessStep = cms.Sequence(process.PixelLessStepTask)


process.TobTecStep = cms.Sequence(process.TobTecStepTask)


process.ctfTracksPixelLess = cms.Sequence(process.pixelLessLayerPairs4PixelLessTracking+process.globalPixelLessSeeds+process.ckfTrackCandidatesPixelLess+process.ctfPixelLess)


process.muonSeededStepDebugInOut = cms.Sequence(process.muonSeededStepDebugInOutTask)


process.muonSeededStepCoreInOut = cms.Sequence(process.muonSeededStepCoreInOutTask)


process.cosmicDCTracksSeq = cms.Sequence(process.cosmicDCTracksSeqTask)


process.JetCoreRegionalStep = cms.Sequence(process.JetCoreRegionalStepTask)


process.iterTracking = cms.Sequence(process.iterTrackingTask)


process.doAlldEdXEstimatorsCosmicTF = cms.Sequence(process.dedxTruncated40CosmicTF+process.dedxHitInfoCosmicTF+process.dedxHarmonic2CosmicTF)


process.LowPtTripletStep = cms.Sequence(process.LowPtTripletStepTask)


process.ctfTracksNoOverlaps = cms.Sequence(process.ckfTrackCandidatesNoOverlaps+process.ctfNoOverlaps)


process.doAlldEdXEstimatorsCTFP5LHC = cms.Sequence(process.dedxTruncated40CTFP5LHC+process.dedxHitInfoCTFP5LHC+process.dedxHarmonic2CTFP5LHC)


process.generalTracksSequence = cms.Sequence(process.generalTracksTask)


process.doAllCosmicdEdXEstimators = cms.Sequence(process.doAlldEdXEstimatorsCTF+process.doAlldEdXEstimatorsCosmicTF+process.doAlldEdXEstimatorsCTFP5LHC)


process.muonSeededStep = cms.Sequence(process.muonSeededStepTask)


process.caloJetsForTrk = cms.Sequence(process.caloJetsForTrkTask)


process.muonSeededStepExtra = cms.Sequence(process.muonSeededStepExtraTask)


process.MixedTripletStep = cms.Sequence(process.MixedTripletStepTask)


process.trackerlocalrecoTop = cms.Sequence(process.siPixelClustersTop+process.siPixelRecHitsTop+process.siStripClustersTop+process.siStripMatchedRecHitsTop+process.topBottomClusterInfoProducerTop)


process.ctftracksP5Top = cms.Sequence(process.combinatorialcosmicseedingtripletsP5Top+process.combinatorialcosmicseedingpairsTOBP5Top+process.combinatorialcosmicseedingpairsTECposP5Top+process.combinatorialcosmicseedingpairsTECnegP5Top+process.combinatorialcosmicseedfinderP5Top+process.simpleCosmicBONSeedingLayersTop+process.simpleCosmicBONSeedsTop+process.combinedP5SeedsForCTFTop+process.ckfTrackCandidatesP5Top+process.ctfWithMaterialTracksP5Top)


process.ConvStep = cms.Sequence(process.ConvStepTask)


process.muonSeededStepDebug = cms.Sequence(process.muonSeededStepDebugTask)


process.iterTrackingEarly = cms.Sequence(process.iterTrackingEarlyTask)


process.muonSeededStepCoreOutIn = cms.Sequence(process.muonSeededStepCoreOutInTask)


process.cosmictracksP5 = cms.Sequence(process.cosmicseedfinderP5+process.cosmicCandidateFinderP5+process.cosmictrackfinderCosmics+process.cosmictrackfinderP5+process.cosmicTrackSplitter+process.splittedTracksP5)


process.DetachedTripletStep = cms.Sequence(process.DetachedTripletStepTask)


process.ctftracksP5Bottom = cms.Sequence(process.combinatorialcosmicseedingtripletsP5Bottom+process.combinatorialcosmicseedingpairsTOBP5Bottom+process.combinatorialcosmicseedingpairsTECposP5Bottom+process.combinatorialcosmicseedingpairsTECnegP5Bottom+process.combinatorialcosmicseedfinderP5Bottom+process.simpleCosmicBONSeedingLayersBottom+process.simpleCosmicBONSeedsBottom+process.combinedP5SeedsForCTFBottom+process.ckfTrackCandidatesP5Bottom+process.ctfWithMaterialTracksP5Bottom)


process.beamhaloTracksSeq = cms.Sequence(process.beamhaloTrackerSeedingLayers+process.beamhaloTrackerSeeds+process.beamhaloTrackCandidates+process.beamhaloTracks)


process.PixelPairStep = cms.Sequence(process.PixelPairStepTask)


process.InitialStepPreSplitting = cms.Sequence(process.InitialStepPreSplittingTask)


process.combinatorialcosmicseedinglayersP5 = cms.Sequence(process.combinatorialcosmicseedingtripletsP5+process.combinatorialcosmicseedingpairsTOBP5+process.combinatorialcosmicseedingpairsTECposP5+process.combinatorialcosmicseedingpairsTECnegP5)


process.goodvertexSkim = cms.Sequence(process.primaryVertexFilter+process.noscraping+process.filterOutLowPt)


process.cosmictracksP5Bottom = cms.Sequence(process.cosmicseedfinderP5Bottom+process.cosmicCandidateFinderP5Bottom+process.cosmictrackfinderP5Bottom)


process.doAlldEdXEstimators = cms.Sequence(process.doAlldEdXEstimatorsTask)


process.DetachedQuadStep = cms.Sequence(process.DetachedQuadStepTask)


process.muonSeededStepExtraInOut = cms.Sequence(process.muonSeededStepExtraInOutTask)


process.InitialStep = cms.Sequence(process.InitialStepTask)


process.trackerlocalrecoBottom = cms.Sequence(process.siPixelClustersBottom+process.siPixelRecHitsBottom+process.siStripClustersBottom+process.siStripMatchedRecHitsBottom+process.topBottomClusterInfoProducerBottom)


process.tracksP5Top = cms.Sequence(process.ctftracksP5Top+process.cosmictracksP5Top)


process.ckftracks_wodEdX = cms.Sequence(process.iterTracking+process.electronSeedsSeq)


process.ckftracks_woBH = cms.Sequence(process.iterTracking+process.electronSeedsSeq+process.doAlldEdXEstimators)


process.ctftracksP5 = cms.Sequence(process.combinatorialcosmicseedinglayersP5+process.combinatorialcosmicseedfinderP5+process.simpleCosmicBONSeedingLayers+process.simpleCosmicBONSeeds+process.combinedP5SeedsForCTF+process.ckfTrackCandidatesP5+process.ctfWithMaterialTracksCosmics+process.ctfWithMaterialTracksP5+process.ckfTrackCandidatesP5LHCNavigation+process.ctfWithMaterialTracksP5LHCNavigation)


process.tracksP5 = cms.Sequence(process.cosmictracksP5+process.ctftracksP5+process.doAllCosmicdEdXEstimators+process.siPixelClusterShapeCache)


process.tracksP5Bottom = cms.Sequence(process.ctftracksP5Bottom+process.cosmictracksP5Bottom)


process.ckftracks = cms.Sequence(process.iterTracking+process.electronSeedsSeq+process.doAlldEdXEstimators)


process.trackerCosmics_TopBot = cms.Sequence(process.trackerlocalrecoTop+process.tracksP5Top+process.trackerlocalrecoBottom+process.tracksP5Bottom)


process.tracksP5_wodEdX = cms.Sequence(process.cosmictracksP5+process.ctftracksP5+process.siPixelClusterShapeCache)


process.ckftracks_plus_pixelless = cms.Sequence(process.ckftracks+process.ctfTracksPixelLess)


process.trackingGlobalReco = cms.Sequence(process.ckftracks+process.trackExtrapolator)


process.p = cms.Path(process.goodvertexSkim+process.myOfflineBeamSpot+process.FinalTrackRefitter+process.BeamSpotChecker+process.PVValidation)



