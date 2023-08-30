Weather Station with M5Stack Core Ink
Opis projektu
Projekt przedstawia stację pogodową zrealizowaną na urządzeniu M5Stack Core Ink. Umożliwia on wyświetlanie aktualnych danych pogodowych dla różnych miast na ekranie e-ink.

Wymagania sprzętowe i oprogramowania
M5Stack Core Ink
Komputer z zainstalowanym UIFlow lub dowolnym środowiskiem programowania dla urządzeń M5Stack
Dostęp do sieci Wi-Fi
Instrukcje instalacji
Sklonuj repozytorium projektu na swój lokalny komputer.
Otwórz plik projektu w UIFlow lub dowolnym środowisku programowania dla urządzeń M5Stack.
Upewnij się, że jesteś połączony z siecią Wi-Fi.
Zaktualizuj klucz API dla usługi OpenWeatherMap w kodzie.
Uruchom program na urządzeniu M5Stack Core Ink.
Sposób użycia
Uruchom urządzenie.
Użyj przycisków na urządzeniu, aby przełączać się między różnymi miastami:
UP: Stavanger
MID: Warszawa
DOWN: Londyn
Funkcjonalności
Wyświetlanie aktualnej temperatury, wilgotności i ciśnienia atmosferycznego.
Graficzna reprezentacja aktualnej pogody (słonecznej, deszczowej).
Możliwość przełączania między różnymi miastami.
Animacje zależne od aktualnej pogody.
Personalizacja i rozwijanie projektu
Chociaż projekt został stworzony z myślą o wyświetlaniu danych pogodowych dla kilku predefiniowanych miast, kod jest dostatecznie elastyczny, aby można go było dostosować do własnych potrzeb. Oto kilka wskazówek:

Dodawanie nowych miast
Znajdź odpowiednią funkcję w kodzie (np. setup_warsaw dla Warszawy).
Skopiuj funkcję i zmodyfikuj ją, aby korzystała z nowego miasta.
Dodaj nową funkcję do logiki przycisków.
Zmiana wyglądu
Kod korzysta z bibliotek M5Stack do tworzenia interfejsu użytkownika.
Możesz edytować różne elementy takie jak M5Circle, M5Rect itd., aby zmienić wygląd interfejsu.
Uwierzytelnianie API
Jeżeli korzystasz z własnego klucza API do OpenWeatherMap, upewnij się, że jest on prawidłowo zaktualizowany w kodzie.
Przykłady działania
Słoneczna pogoda:
Słoneczna pogoda

Deszczowa pogoda:
