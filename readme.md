# Weather Station with M5Stack Core Ink

## Opis projektu

Projekt przedstawia stację pogodową zrealizowaną na urządzeniu M5Stack Core Ink. Umożliwia on wyświetlanie aktualnych danych pogodowych dla różnych miast na ekranie domyślnie dla miast (Stavanger, Londyn, Warszawa).

## Wymagania sprzętowe i oprogramowania

- M5Stack Core Ink lub inne urządzenia M5Stack
- Komputer z zainstalowanym UIFlow lub dowolnym środowiskiem programowania dla urządzeń M5Stack
- Dostęp do sieci Wi-Fi

## Instrukcje instalacji

1. Sklonuj repozytorium projektu na swój lokalny komputer.
2. Otwórz plik projektu w UIFlow lub dowolnym środowisku programowania dla urządzeń M5Stack.
3. Upewnij się, że poprawnie zaaktualizowałeś dane dla Twojego WiFi, aby urządzenie M5Stack miało dostęp do internetu.
4. Zaktualizuj klucz API dla usługi OpenWeatherMap w kodzie.
5. Uruchom program na urządzeniu M5Stack.

## Sposób użycia

- Uruchom urządzenie.
- Urządzenie trafii do pętli w której do póki nie połączy się z internetem nie przejdzie dalej.
- Użyj przycisków na urządzeniu, aby przełączać się między różnymi miastami:
  - UP: Stavanger
  - MID: Warszawa
  - DOWN: Londyn

## Funkcjonalności

- Wyświetlanie aktualnej temperatury, wilgotności i ciśnienia atmosferycznego.
- Graficzna reprezentacja aktualnej pogody (słonecznej, deszczowej, pochmurnej).
- Możliwość przełączania między różnymi miastami.
- Animacje zależne od aktualnej pogody.

## Personalizacja i rozwijanie projektu

Chociaż projekt został stworzony z myślą o wyświetlaniu danych pogodowych dla kilku predefiniowanych miast (Stavanger, Londyn, Warszawa), kod jest dostatecznie elastyczny, aby można go było dostosować do własnych potrzeb. Oto kilka wskazówek:

### Dodawanie nowych miast
- Znajdź odpowiednią funkcję w kodzie (np. `setup_warsaw` dla Warszawy).
- Skopiuj funkcję i zmodyfikuj ją, aby korzystała z nowego miasta.
- Dodaj nową funkcję do logiki przycisków.

### Zmiana wyglądu
- Kod korzysta z bibliotek M5Stack do tworzenia interfejsu użytkownika.
- Możesz edytować różne elementy takie jak `M5Circle`, `M5Rect` itd., aby zmienić wygląd interfejsu.
- Ewentualnie kontynnuować programowanie w wygenerowanym kodzie python, który jest dołączony do repozytorium.

### Uwierzytelnianie API
- Jeżeli korzystasz z własnego klucza API do OpenWeatherMap, upewnij się, że jest on prawidłowo zaktualizowany w kodzie.

## Aktualizacja danych WiFi
- Upewnij się, żeby w kodzie zmienić dane do Twojej lokalnej sieci.

## Przykłady działania

- Słoneczna pogoda:
  Wkrótce zostanię udostępnione fizyczne zdj...
  
- Deszczowa pogoda:
 Wkrótce zostanię udostępnione fizyczne zdj...
