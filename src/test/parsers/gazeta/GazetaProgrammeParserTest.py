# -*- coding: utf-8 -*-
from epguide.parsers.gazeta import GazetaProgrammeParser
import datetime
import unittest
import codecs
from epguide.data_formats import ParserOptions
from epguide.util import to_string

class  GazetaProgrammeParserTest(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None 
        pass

    def tearDown(self):
        pass

    def testChannel(self):
        p = GazetaProgrammeParser.GazetaProgrammeParser(ParserOptions())
        f = codecs.open("TVP-1.html", "r", "ISO-8859-2")
        buf = f.read()
        eventDate = datetime.datetime(2013, 1, 1)
        channel_id = "TVP-1"
        events = [to_string(c) for c in p.get_events(eventDate, channel_id, buf)]
        f.close()
        
        print 'actual events:\n[\n"' + '",\n"'.join(events) + '"\n]'
        
        expected = [
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 05:20:00', time_end:'2013-01-01 05:55:00', title:'Po prostu. Program Tomasza Sekielskiego', subtitle:None, episode_num:None, category:'Program publicystyczny', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717481,Po_prostu_Program_Tomasza_Sekielskiego.html', desc:'Autorski program publicystyczno-reporterski, w którym poruszane\\n są najważniejsze tematy społeczno-polityczne. W każdym odcinku widzowie\\n zobaczą też wywiady z nietuzinkowymi osobami.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 05:55:00', time_end:'2013-01-01 08:00:00', title:'Info poranek', subtitle:None, episode_num:None, category:'Magazyn informacyjny', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717482,Info_poranek.html', desc:None, details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 08:00:00', time_end:'2013-01-01 08:05:00', title:'Wiadomości', subtitle:None, episode_num:None, category:'Wiadomości', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717483,Wiadomosci.html', desc:'Serwis prezentuje najważniejsze informacje z kraju i ze świata.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 08:05:00', time_end:'2013-01-01 08:10:00', title:'Pogoda poranna', subtitle:None, episode_num:None, category:'Pogoda', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717484,Pogoda_poranna.html', desc:None, details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 08:10:00', time_end:'2013-01-01 08:25:00', title:'Polityka przy kawie', subtitle:None, episode_num:None, category:'Program publicystyczny', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717485,Polityka_przy_kawie.html', desc:'W programie rozmowy z politykami na temat ostatnich ważnych wydarzeń w kraju.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 08:25:00', time_end:'2013-01-01 08:55:00', title:'Telezakupy', subtitle:None, episode_num:None, category:'Program reklamowy', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717486,Telezakupy.html', desc:'Magazyn reklamowy prezentujący artykuły gospodarstwa domowego, \\nurządzenia do poprawy kondycji i zdrowia. Po zapoznaniu się z ofertą \\nwidzowie mogą telefonicznie zamówić wybrane towary.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 08:55:00', time_end:'2013-01-01 09:55:00', title:'Ojciec Mateusz', subtitle:None, episode_num:None, category:'Serial kryminalny', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717487,Ojciec_Mateusz.html', desc:'Grupa grafficiarzy pojawiła się w Sandomierzu. Jeden z nich \\nzostaje oskarżony o zabójstwo mieszkańca, z którym grupa miała zatarg. \\nKs. Mateusz nie wierzy w winę chłopaka i rozpoczyna śledztwo.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 09:55:00', time_end:'2013-01-01 11:00:00', title:'Moksgmol - biały baribal', subtitle:None, episode_num:None, category:'Film dokumentalny', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717488,Moksgmol__bialy_baribal.html', desc:'Great Bear Rainforest w Kolumbii Brytyjskiej to jeden z \\nnajwiększych na świecie lasów deszczowych strefy umiarkowanej. Żyją tu \\nniedźwiedzie, wilki i wiele innych niezwykłych gatunków zwierząt.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 11:00:00', time_end:'2013-01-01 12:00:00', title:'Świat się kręci', subtitle:None, episode_num:None, category:'Magazyn', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717489,Swiat_sie_kreci.html', desc:'Codzienny program studyjny poruszający tematy społeczno-polityczne, naukowe, kulturalne, a także rozrywkowe.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 12:00:00', time_end:'2013-01-01 12:15:00', title:'Wiadomości', subtitle:None, episode_num:None, category:'Wiadomości', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717490,Wiadomosci.html', desc:'Serwis prezentuje najważniejsze informacje z kraju i ze świata.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 12:15:00', time_end:'2013-01-01 12:45:00', title:'Agrobiznes', subtitle:None, episode_num:None, category:'Magazyn rolniczy', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717491,Agrobiznes.html', desc:'Dziennik informacyjny przeznaczony głównie dla biznesmenów \\npracujących w otoczeniu rolnictwa, rolników, handlowców, ale także dla \\nmieszkańców miast.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 12:45:00', time_end:'2013-01-01 13:50:00', title:'Dzikie oblicze Andów', subtitle:None, episode_num:None, category:'Film dokumentalny', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717492,Dzikie_oblicze_Andow.html', desc:'Dokument opowiada o poszukiwaniu cudów natury i historii \\nzwierząt zamieszkujących Andy, największy łańcuch górski na świecie, \\nrozciągający się na przestrzeni 9000 kilometrów.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 13:50:00', time_end:'2013-01-01 14:20:00', title:'Jaka to melodia?', subtitle:None, episode_num:None, category:'Teleturniej muzyczny', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717493,Jaka_to_melodia.html', desc:'W teleturnieju bierze udział 3 uczestników, z których jeden \\njest finalistą poprzedniego odcinka. Finalista może pojawić się najwyżej\\n 3 razy pod rząd w kolejnych programach.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 14:20:00', time_end:'2013-01-01 15:00:00', title:'Moda na sukces', subtitle:None, episode_num:None, category:'Telenowela', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717494,Moda_na_sukces.html', desc:'Thorne obwieszcza Stephanie, Erykowi i Ridge'owi, że nie jest \\nojcem Liama i bardzo tego żałuje. Oliver chce odejść z firmy. Bill \\nzapewnia Liama, że nie porzucił jego matki. To ona odeszła.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 15:00:00', time_end:'2013-01-01 15:10:00', title:'Wiadomości', subtitle:None, episode_num:None, category:'Wiadomości', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717495,Wiadomosci.html', desc:'Serwis prezentuje najważniejsze informacje z kraju i ze świata.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 15:10:00', time_end:'2013-01-01 15:15:00', title:'Pogoda', subtitle:None, episode_num:None, category:'Pogoda', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717496,Pogoda.html', desc:'Codzienny serwis informacyjny z prognozą pogody.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 15:15:00', time_end:'2013-01-01 15:45:00', title:'Klan', subtitle:None, episode_num:None, category:'Telenowela', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717497,Klan.html', desc:'Kasia wdraża sekretny plan w życie i uzyskuje zgodę matki na \\nnocleg u Basi. Paweł składa Alicji kondolencje z powodu śmierci męża. \\nOkazuje się, że mężczyzna, który zginął w wypadku, to nie Marczyński.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 15:45:00', time_end:'2013-01-01 16:40:00', title:'Drużyna A', subtitle:None, episode_num:None, category:'Serial sensacyjny', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717498,Druzyna_A.html', desc:'Dwie koleżanki z college'u angażują Drużynę A, by odbiła ich \\nprofesora z rąk mafii hazardowej. Udając oddział specjalny, B.A. i \\nMurdock ruszają do Las Vegas, by przejąć bossa mafii.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 16:40:00', time_end:'2013-01-01 17:00:00', title:'Polska non stop', subtitle:None, episode_num:None, category:'Magazyn reporterów', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717499,Polska_non_stop.html', desc:'Prezentacja informacji dotyczących aktualnych wydarzeń, przede \\nwszystkim krajowych. Reportaże o najważniejszych i najbardziej \\ninteresujących sprawach bieżących oraz reportaże interwencyjne.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 17:00:00', time_end:'2013-01-01 17:15:00', title:'Teleexpress', subtitle:None, episode_num:None, category:'Wiadomości', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717500,Teleexpress.html', desc:'Serwis informacyjny prezentujący aktualne wydarzenia, wiadomości kulturalne oraz ciekawostki z kraju i ze świata.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 17:15:00', time_end:'2013-01-01 17:20:00', title:'Pogoda', subtitle:None, episode_num:None, category:'Pogoda', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717501,Pogoda.html', desc:'Codzienny serwis informacyjny z prognozą pogody.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 17:20:00', time_end:'2013-01-01 17:55:00', title:'Jaka to melodia?', subtitle:None, episode_num:None, category:'Teleturniej muzyczny', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717502,Jaka_to_melodia.html', desc:'W teleturnieju bierze udział 3 uczestników, z których jeden \\njest finalistą poprzedniego odcinka. Finalista może pojawić się najwyżej\\n 3 razy pod rząd w kolejnych programach.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 17:55:00', time_end:'2013-01-01 18:30:00', title:'Klan', subtitle:None, episode_num:None, category:'Telenowela', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717503,Klan.html', desc:'Wieści o Marczyńskim docierają do Leszka. Zaczyna on snuć \\nteorie spiskowe. Matka koleżanki Kasi dzwoni do Grażynki z informacją o \\nwypadku kolejowym pociągu, którym Kasia i Basia podróżowały.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 18:30:00', time_end:'2013-01-01 19:20:00', title:'Świat się kręci', subtitle:None, episode_num:None, category:'Magazyn', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717504,Swiat_sie_kreci.html', desc:'Codzienny program studyjny poruszający tematy społeczno-polityczne, naukowe, kulturalne, a także rozrywkowe.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 19:20:00', time_end:'2013-01-01 19:30:00', title:'Przepis dnia', subtitle:None, episode_num:None, category:'Magazyn kulinarny', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717505,Przepis_dnia.html', desc:None, details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 19:30:00', time_end:'2013-01-01 20:00:00', title:'Wiadomości', subtitle:None, episode_num:None, category:'Wiadomości', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717506,Wiadomosci.html', desc:'Serwis prezentuje najważniejsze informacje z kraju i ze świata.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 20:00:00', time_end:'2013-01-01 20:10:00', title:'Sport', subtitle:None, episode_num:None, category:'Wiadomości sportowe', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717507,Sport.html', desc:'Informacje o najważniejszych wydarzeniach sportowych.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 20:10:00', time_end:'2013-01-01 20:20:00', title:'Pogoda', subtitle:None, episode_num:None, category:'Pogoda', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717508,Pogoda.html', desc:'Codzienny serwis informacyjny z prognozą pogody.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 20:20:00', time_end:'2013-01-01 20:25:00', title:'Piąty stadion', subtitle:None, episode_num:None, category:'Serial komediowy', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717509,Piaty_stadion.html', desc:'Serial opowiada o grupie przyjaciół - miłośników piłki nożnej, \\nktórzy spędzają dużo czasu w pubie \"Piąty Stadion\". Perypetie bohaterów \\nobfitują w zabawne i nieprzewidywalne sytuacje.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 20:25:00', time_end:'2013-01-01 20:40:00', title:'Real Madryt - Galatasaray SK', subtitle:None, episode_num:None, category:'Piłka nożna', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717510,Real_Madryt__Galatasaray_SK.html', desc:'W 5. kolejce meczów fazy grupowej LM Real Madryt spotka się z \\nGalatasarayem. Kibice wicemistrza Hiszpanii liczą, że Królewscy powtórzą\\n wynik ze Stambułu, gdzie 17 września 2013 roku wygrali 6:1.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 20:40:00', time_end:'2013-01-01 23:00:00', title:'Real Madryt - Galatasaray SK', subtitle:None, episode_num:None, category:'Piłka nożna', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717511,Real_Madryt__Galatasaray_SK.html', desc:'W 5. kolejce meczów fazy grupowej LM Real Madryt spotka się z \\nGalatasarayem. Kibice wicemistrza Hiszpanii liczą, że Królewscy powtórzą\\n wynik ze Stambułu, gdzie 17 września 2013 roku wygrali 6:1.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 23:00:00', time_end:'2013-01-01 23:05:00', title:'Liga Mistrzów', subtitle:None, episode_num:None, category:'Piłka nożna', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717512,Liga_Mistrzow.html', desc:None, details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 23:05:00', time_end:'2013-01-01 23:40:00', title:'Liga Mistrzów', subtitle:None, episode_num:None, category:'Piłka nożna', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717513,Liga_Mistrzow.html', desc:None, details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 23:40:00', time_end:'2013-01-01 23:50:00', title:'Liga Mistrzów', subtitle:None, episode_num:None, category:'Piłka nożna', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717514,Liga_Mistrzow.html', desc:None, details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-01 23:50:00', time_end:'2013-01-02 00:45:00', title:'Transporter', subtitle:None, episode_num:None, category:'Serial sensacyjny', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717515,Transporter.html', desc:None, details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-02 00:45:00', time_end:'2013-01-02 01:45:00', title:'Drużyna A', subtitle:None, episode_num:None, category:'Serial sensacyjny', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717516,Druzyna_A.html', desc:'Dwie koleżanki z college'u angażują Drużynę A, by odbiła ich \\nprofesora z rąk mafii hazardowej. Udając oddział specjalny, B.A. i \\nMurdock ruszają do Las Vegas, by przejąć bossa mafii.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-02 01:45:00', time_end:'2013-01-02 02:40:00', title:'Świat się kręci', subtitle:None, episode_num:None, category:'Magazyn', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717517,Swiat_sie_kreci.html', desc:'Codzienny program studyjny poruszający tematy społeczno-polityczne, naukowe, kulturalne, a także rozrywkowe.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-02 02:40:00', time_end:'2013-01-02 04:20:00', title:'Doskonałe popołudnie', subtitle:None, episode_num:None, category:'Dramat obyczajowy', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717518,Doskonale_popoludnie.html', desc:'Mikołaj i Anna mają się pobrać, lecz nie znajdują czasu na \\nprzygotowania do ślubu. Są pochłonięci pracą w swoim wydawnictwie. \\nTymczasem do matki Mikołaja po 12 latach powraca mąż.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-02 04:20:00', time_end:'2013-01-02 04:30:00', title:'Notacje', subtitle:None, episode_num:None, category:'Serial dokumentalny', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4717519,Notacje.html', desc:'Cykl programów, w których zasłużone dla Polski osoby opowiadają\\n o jednym epizodzie ze swojego życia. Bohaterką odcinka jest Barbara \\nKasprowicz.', details:None)",
"GazetaEvent(channel_id:'TVP-1', channel_name:'TVP 1', time_start:'2013-01-02 04:30:00', time_end:'2013-01-02 04:30:00', title:'Przerwa w nadawaniu', subtitle:None, episode_num:None, category:'Przerwa w emisji', url:'http://tv.gazeta.pl/program_tv/0,110740,8651580,,,4739461,Przerwa_w_nadawaniu.html', desc:None, details:None)"
]
        self.assertEqual(events, expected)


if __name__ == '__main__':
    unittest.main()
