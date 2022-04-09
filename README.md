# TDD in Python 

Dit is een proef met TDD in Python onder het mom van persoonlijke innovatie. 

## Achtergrond
Er is een TDD workshop die Eric verder ontwikkeld heeft obv een YouTube video, deze workshop vond Eric 
toegevoege waarde voor zijn persoonlijke workflow als het om ontwikkelen van Test automatiserings scripts gaat. Deze 
workshop is echter in JAVA en al een tijdje niet aangeraakt. 

Vanuit het GTO willen we ruimte geven aan persoonlijke innovatie. Dit ticket is er om te kijken hoe Python werkt met TDD. 
Voor Eric is dit zoeken omdat hij veel meer comfortabel is in JAVA. 

Toch weet Eric uit persoonlijke ervaring dat er veel toegevoegde waarde zit in de TDD mindset. 
Maakt dan ook niet uit met welke programmeertaal dan ook. Er zijn vast ook veel handige tools voor Python 
die hiermee kunnen helpen. 

## Doelstelling
Doelstelling van deze map/repo is om kennis te delen hierover met de rest van het team. 
Het is niet de bedoeling om de gehele JAVA workshop te herschrijven naar Python. Maar wel om te zien hoe de opstart (de 
eerste paar stappen binnen dit proces werken in Python). 

# Voorbeelden van verschillen JAVA/Python
Ter illustratie, een eerste test op pagina 12 van REF#1

Voorbeeld JAVA
```
@Test
public void itemCanBeAddedToTheBasket() throws Exception{
    Basket basket = new Basket();
    basket.add(new Object()); 
    basket.add(new Object()); 
    assertEquals(2, basket.size());
}
```
Vertaalt zich zo ongeveer naar dit in Python.

Voorbeeld Python 
```
class TestBasket(unittest.TestCase):

    def test_add(self):
        basket_instance = Basket.ShoppingBasket
        basket_instance.add(self)
        basket_instance.add(self)
        self.assertEqual(2, basket_instance.Basket.size)
```
Zoals je kan zien, op het oog niet veel verschillend maar er zijn zeker verschillen qua syntax. Dus dat is al waardevol
om te leren. Ook denken in hoe je x doet in Python vs JAVA is al waardevol. 


## Referentiemateriaal

- REF#1 [Link naar de workshop in JAVA](./referentie/Dive-into-TDD-JAVA.pdf)
- REF#2 [Link naar de oorspronkelijke video](https://www.youtube.com/watch?v=PIWLC3dexSA)

