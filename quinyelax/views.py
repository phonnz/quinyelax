# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.mail import send_mail

from models import *

def home(request):

	# paises = (('151','Afganistán'),('2','Albania'),('17','Alemania'),('3','Andorra'),('98','Angola'),('53','Anguilla'),('54','Antigua y Barbuda'),('73','Antillas Holandesas'),('194','Arabia Saudí'),('97','Argelia'),('81','Argentina'),('182','Armenia'),('55','Aruba'),('197','Australia'),('4','Austria'),('183','Azerbayan'),('56','Bahamas'),('184','Bahrain'),('152','Bangladesh'),('57','Barbados'),('6','Bélgica'),('58','Belice'),('99','Benin'),('48','Bermudas'),('5','Bielorrusia'),('82','Bolivia'),('7','Bosnia - Herzegovina'),('100','Botswana'),('83','Brasil'),('154','Brunei'),('8','Bulgaria'),('101','Burkina Faso'),('155','Burma (Myanmar)'),('102','Burundi'),('153','Bután'),('104','Cabo Verde'),('156','Camboya'),('103','Camerún'),('49','Canada'),('106','Chad'),('84','Chile'),('157','China'),('10','Chipre'),('85','Colombia'),('107','Comoros'),('108','Congo'),('170','Corea del Norte'),('174','Corea del Sur'),('217','Costa de Marfil'),('60','Costa Rica'),('9','Croacia'),('61','Cuba'),('12','Dinamarca'),('62','Dominica'),('86','Ecuador'),('110','Egipto'),('64','El Salvador'),('195','Emiratos Arabes Unidos'),('112','Eritrea'),('39','Eslovaquia'),('40','Eslovenia'),('1','España'),('52','Estados Unidos'),('13','Estonia'),('113','Etiopia'),('199','Fiji'),('172','Filipinas'),('15','Finlandia'),('16','Francia'),('114','Gabón'),('115','Gambia'),('185','Georgia'),('116','Ghana'),('18','Gibraltar'),('65','Granada'),('19','Grecia'),('50','Groenlandia'),('66','Guadalupe'),('201','Guam'),('67','Guatemala'),('90','Guayana'),('88','Guayana Francesa'),('117','Guinea'),('111','Guinea Ecuatorial'),('118','Guinea-Bissau'),('68','Haití'),('32','Holanda'),('69','Honduras'),('158','Hong Kong'),('20','Hungría'),('59','I. Caimán'),('219','I. Cocos (Keeling)'),('198','I. Cook'),('14','I. Feroe'),('89','I. Galápagos'),('87','I. Malvinas'),('203','I. Marianas del Norte'),('204','I. Marshall'),('133','I. Reunión'),('212','I. Salomón'),('218','I. Vírgenes Británicas'),('80','I. Vírgenes EEUU'),('216','I. Wallis y Futuna'),('159','India'),('160','Indonesia'),('186','Irán'),('187','Iraq'),('22','Irlanda'),('21','Islandia'),('188','Israel'),('23','Italia'),('70','Jamaica'),('161','Japón'),('189','Jordania'),('162','Kazajistán'),('119','Kenia'),('163','Kirguizistán'),('202','Kiribati'),('190','Kuwait'),('164','Laos'),('120','Lesotho'),('24','Letonia'),('191','Líbano'),('121','Liberia'),('122','Líbia'),('25','Liechtenstein'),('26','Lituania'),('27','Luxemburgo'),('165','Macao'),('28','Macedonia'),('123','Madagascar'),('166','Malasia'),('124','Malawi'),('167','Maldivas'),('125','Mali'),('29','Malta'),('128','Marruecos'),('71','Martinica'),('127','Mauricio'),('126','Mauritania'),('51','México'),('205','Micronesia'),('30','Moldavia'),('31','Mónaco'),('168','Mongolia'),('72','Montserrat'),('129','Mozambique'),('130','Namibia'),('206','Nauru'),('169','Nepal'),('74','Nicaragua'),('131','Níger'),('132','Nigeria'),('33','Noruega'),('207','Nueva Caledonia'),('208','Nueva Zelanda'),('192','Omán'),('171','Pakistán'),('209','Palau'),('75','Panamá'),('210','Papua Nueva Guinea'),('91','Paraguay'),('92','Peru'),('200','Polinesia Francesa'),('34','Polonia'),('35','Portugal'),('76','Puerto Rico'),('193','Qatar'),('45','Reino Unido'),('105','Rep. Centroafricana'),('11','Rep. Checa'),('63','Rep. Dominicana'),('134','Ruanda'),('36','Rumania'),('37','Rusia'),('147','Sáhara Occidental'),('211','Samoa'),('38','San Marino'),('135','Sao Tomé y Príncipe'),('136','Senegal'),('137','Seychelles'),('138','Sierra Leona'),('173','Singapur'),('220','Siria'),('139','Somalia'),('175','Sri Lanka'),('78','St. Vicent y Grenadines'),('77','St.Kitts & Nevis'),('141','Sudán'),('41','Suecia'),('42','Suiza'),('93','Sur Georgia e I. Sandwich'),('140','Suráfrica'),('94','Surinam'),('142','Swazilandia'),('178','Tailandia'),('176','Taiwán'),('177','Tajikistán'),('143','Tanzania'),('144','Togo'),('213','Tonga'),('79','Trinidad y Tobago'),('145','Túnez'),('179','Turkmenistán'),('43','Turquia'),('214','Tuvalu'),('44','Ucrania'),('146','Uganda'),('95','Uruguay'),('180','Uzbekistán'),('215','Vanuatu'),('46','Vaticano'),('96','Venezuela'),('181','Vietnam'),('196','Yemen'),('109','Yibuti'),('47','Yugoslavia'),('148','Zaire'),('149','Zambia'),('150','Zimbabwe'))
    # for p in paises:
    # 	pais = Country()
    # 	pais.name = p[1]
    # 	print pais.name
    # 	pais.save()

    # eq1 = Team()
    # eq1.name = 'México'
    # eq1.group = 'A'
    # eq1.save()

    # eq1 = Team()
    # eq1.name = 'México'
    # eq1.group = 'B'
    # eq1.save()

    # eq1 = Team()
    # eq1.name = 'México'
    # eq1.group = 'C'
    # eq1.save()

    # eq1 = Team()
    # eq1.name = 'México'
    # eq1.group = 'D'
    # eq1.save()

    # eq1 = Team()
    # eq1.name = 'México'
    # eq1.group = 'E'
    # eq1.save()
	
	groups = []
	a = Team.objects.filter(group = 'A')
	b = Team.objects.filter(group = 'B')
	c = Team.objects.filter(group = 'C')
	d = Team.objects.filter(group = 'D')
	e = Team.objects.filter(group = 'E')
	f = Team.objects.filter(group = 'F')
	g = Team.objects.filter(group = 'G')
	h = Team.objects.filter(group = 'H')

	groups.append(a)
	groups.append(b)
	groups.append(c)
	groups.append(d)
	groups.append(e)
	groups.append(f)
	groups.append(g)
	groups.append(h)
	

	return render(request, 'index.html',{ 'groups':groups })



def send_Mail(email):
	
	send_mail('Registro exitoso', u'Se registró %s' % email ,'quinyelax@effio.la', ('agonzalez@nyxtechnology.com',), fail_silently=False)