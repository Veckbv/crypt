"""vkupu zts t vthwu suv xlv lfqup t vpuu bf ipxfv xi vku kxlsu tfq vku ntpek ktpu tfq vku ktvvup zupu ktabfc vut tv bv t qxpnxlsu zts sbvvbfc huvzuuf vkun itsv tswuuj tfq vku xvkup vzx zupu lsbfc bv ts t elskbxf pusvbfc vkubp uwhxzs xf bv tfq vtwobfc xaup bvs kutq aupd lfexnixpvthwu ixp vku qxpnxlsu vkxlckv twbeu xfwd ts bvs tswuuj b sljjxsu bv qxusfv nbfq

vku vthwu zts t wtpcu xfu hlv vku vkpuu zupu tww epxzquq vxcuvkup tv xfu expfup xi bv fx pxxn fx pxxn vkud epbuq xlv zkuf vkud stz twbeu exnbfc vkupus jwufvd xi pxxn stbq twbeu bfqbcftfvwd tfq sku stv qxzf bf t wtpcu tpnektbp tv xfu ufq xi vku vthwu

ktau sxnu zbfu vku ntpek ktpu stbq bf tf ufexlptcbfc vxfu

twbeu wxxouq tww pxlfq vku vthwu hlv vkupu zts fxvkbfc xf bv hlv vut b qxfv suu tfd zbfu sku puntpouq

vkupu bsfv tfd stbq vku ntpek ktpu

vkuf bv ztsfv aupd ebabw xi dxl vx xiiup bv stbq twbeu tfcpbwd

bv ztsfv aupd ebabw xi dxl vx sbv qxzf zbvkxlv hubfc bfabvuq stbq vku ntpek ktpu

b qbqfv ofxz bv zts dxlp vthwu stbq twbeu bvs wtbq ixp t cputv ntfd nxpu vktf vkpuu

dxlp ktbp ztfvs elvvbfc stbq vku ktvvup ku ktq huuf wxxobfc tv twbeu ixp sxnu vbnu zbvk cputv elpbxsbvd tfq vkbs zts kbs ibpsv sjuuek

dxl skxlwq wutpf fxv vx ntou jupsxftw puntpos twbeu stbq zbvk sxnu suaupbvd bvs aupd plqu tfq iwtcbstwbeuplwugg"""


Вычислим частоту встречаемости отдельных букв в этом шифротексте(с помощью python)
[('u', 12.865497076023392), ('v', 10.33138401559454), ('t', 9.551656920077972), ('b', 7.894736842105263), ('x', 7.309941520467836), ('f', 6.82261208576998), ('p', 6.725146198830409), ('k', 5.750487329434698), ('s', 5.750487329434698), ('w', 3.8011695906432745), ('q', 3.8011695906432745), ('l', 2.631578947368421), ('z', 2.53411306042885), ('e', 2.53411306042885), ('n', 2.241715399610136), ('c', 2.046783625730994), ('d', 1.949317738791423), ('i', 1.5594541910331383), ('h', 1.267056530214425), ('a', 1.0721247563352825), ('j', 0.682261208576998), ('o', 0.682261208576998), ('g', 0.1949317738791423)]

Вычислим наиболее употребительные биграммы в шифрофке(с помощью python)
[('vk', 3.216374269005848), ('ku', 2.8265107212475633), ('up', 2.144249512670565), ('bv', 2.144249512670565), ('pu', 1.949317738791423), ('bf', 1.8518518518518516), ('xl', 1.461988304093567), ('tf', 1.461988304093567), ('tp', 1.364522417153996), ('ts', 1.267056530214425)]

Вычислим наиболее употребительные триграммы в шифрофке(с помощью python)
[('vku', 2.3391812865497075), ('bfc', 1.0721247563352825), ('twb', 0.8771929824561403), ('wbe', 0.8771929824561403), ('beu', 0.8771929824561403), ('tbq', 0.8771929824561403), ('zts', 0.7797270955165692), ('stb', 0.7797270955165692), ('upu', 0.682261208576998), ('tfq', 0.682261208576998)]

Буква 'u' имеет самую высокую частоту(12.865), можно предположить, что она соответствует букве 'e' открытого текста. 
Посмотрим, что это может означать для наиболее общих триграмм шифротекста.
- Триграмма 'vku' соответствует 'vke' исходного сообщения
- Триграмма 'beu' -> 'bee'
- Триграмма 'upu' -> 'epe'

Посмотрим теперь на часто употребляемые триграммы в английском языке и выберем из них те, которые начинаются и оканчиваются на букву 'e' или заканчиваются на букву 'e' : 'the', 'ere', 'ate'
Из самых часто встречающихся триграм, только одна триграмма начинается и заканчивается с буквы 'e': 'ere' и только две заканчиваются на 'e', но 'the' встречается в 6 раз чаще, чем 'ate', а также биграмма имеющая самую высокую частоту является 'vk', можно предположить с выской долей вероятности, что имеет место соответствие 'p' = 'r', 'k' = 'h'

Посмотрим , что это может означать для наиболее общих биграмм шифротекста.
- 'ku' -> 'he'
- 'up' -> 'er'
- 'pu' -> 're'
- 'tp' -> 'tr' 

Ограничившись первым абзацем, произведем в них замены найденных соответствий, считая, что нашли их правильно.

'vhere zts t vthwe sev xlv lfqer t vree bf irxfv xi vhe hxlse tfq vhe ntreh htre tfq vhe htvver zere htabfc vet tv bv t qxrnxlse zts sbvvbfc hevzeef vhen itsv tsweej tfq vhe xvher vzx zere lsbfc bv ts t elshbxf resvbfc vhebr ewhxzs xf bv tfq vtwobfc xaer bvs hetq aerd lfexnixrvthwe ixr vhe qxrnxlse vhxlchv twbee xfwd ts bvs tsweej b sljjxse bv qxesfv nbfq'

Получившееся первое слово 'vhere' очень похоже на английское 'there', можно с высокой долей вероятности предположить, что 'v' = 't'

Посмотрим, что это может означать для наиболее общих биграмм шифротекста.
- 'bv' -> 'bt'

Посмотрим теперь на часто употребляемые биграммы в английском языке и выберем из них те, которые оканчиваются на букву 't' или не начинаются на уже известные буквы : 'nt', 'it'. Можно предположить с высокой долей вероятности, что 'b' = 'n'

В шифровке буква 't' появляется как отдельное слово, она может замещать лишь одну из двух букв открытоо текста: 'i' или 'a'. Частота буквы 't' в шифротексте - 6.822, а среднестатистические частоты букв 'i' и 'a' = 7.0 и 8.2. Следовательно, скорее всего 't' = 'a'. 
Посмотрим, что это может означать для наиболее общих триграмм шифротекста.
- Триграмма 'twb' соответствует 'awn' исходного сообщения
- Триграмма 'tbq'(0.877) -> 'anq'
- Триграмма 'zts'(0.779) -> 'zas'
- Триграмма 'stb'(0.779) -> 'san'
- Триграмма 'tfq'(0.682) -> 'afq'

Посмотрим теперь на часто употребляемые триграммы в английском языке и выберем из них те, которые начинаются на букву 'a' или буква 'a' находится в середине : 'and'(0.73), 'ati', 'hat', 'ate', 'all'. Можно сделать вывод, что 'anq' = 'and' и получается, что 'q' = 'd'.

Проведем замены уже вычисленных букв в пером абзаце.

'there was a tahwe set xlt lfder a tree bf irxft xi the hxlse afd the nareh hare afd the hatter were haabfc tea at bt a dxrnxlse was sbttbfc hetweef then iast asweej afd the xther twx were lsbfc bt as a elshbxf restbfc thebr ewhxws xf bt afd tawobfc xaer bts head aerd lfexnixrtahwe ixr the dxrnxlse thxlcht awbee xfwd as bts asweej b sljjxse bt dxesft nbfd'

Второе слово похоже на часто встречающуюся триграм в английском языке 'was', можно предположить, что 'z' = 'w'
В шифротексте часто встречается слово 'afd', можно предположить, что это 'and', а это значит, что 'b' = 'i', а не 'b' и следовательно 'f' = 'n'

Смотрим, что получилось 

'there was a tahwe set xlt lnder a tree in irxnt xi the hxlse and the nareh hare and the hatter were haainc tea at it a dxrnxlse was sittinc hetween then iast asweej and the xther twx were lsinc it as a elshixn restinc their ewhxws xn it and tawoinc xaer its head aerd lnexnixrtahwe ixr the dxrnxlse thxlcht awiee xnwd as its asweej i sljjxse it dxesnt nind'

Слово 'lnder' с высокой долей вероятности является словом 'under', а это значит, что 'l' = 'u'