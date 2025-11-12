# Sistem conversational interactiv cu avatar animat

## [Vezi mai multe detalii despre proiect, inclusiv teaser-ul](PROJECT.md)

## Cuprins

1. [Definirea problemei](#1-definirea-problemei)
2. [Structura generala a sistemului](#2-structura-generala-a-sistemului)
3. [Analiza datelor de intrare](#3-analiza-datelor-de-intrare)
4. [Fluxul de procesare](#4-fluxul-de-procesare)
5. [Extensibilitate si dezvoltari viitoare](#5-extensibilitate-si-dezvoltari-viitoare)
6. [Resurse utile](#6-resurse-utile)
7. [Teaser video](#7-teaser-video)

---

## 1. Definirea problemei

Scopul acestui proiect este dezvoltarea unui **sistem conversational interactiv**, in care un avatar animat raspunde vocal la intrebarile utilizatorului. Sistemul integreaza tehnologii moderne pentru procesarea limbajului natural, sinteza vocala si generare de imagini, cu obiectivul de a oferi o experienta naturala si realista de interactiune om-calculator.

---

## 2. Structura generală a sistemului

Sistemul este organizat modular, fiecare componentă având rolul său bine definit:

Procesare întrebări: preia întrebările utilizatorului și generează răspunsuri folosind un model de limbaj (LLM).

Gestionare avatar: animăm fețele avatarului folosind SadTalker, pornind de la o imagine statică de referință.

Recunoaștere și transcriere vocală (Speech-to-Text, STT): OpenAi Whisper.

Sin​​teza vocală (Text-to-Speech, TTS): convertim răspunsul textual în audio folosind OpenAI Whisper.

Sincronizare audio-video: combinăm animația feței generate de SadTalker cu răspunsul audio pentru a crea videoclipul animat final.

---

## 3. Analiza datelor de intrare

Sistemul va procesa urmatoarele tipuri de date de intrare:

- **Intrebari textuale ale utilizatorului:**  
  Text furnizat direct.

  Fișier audio care poate fi transcris prin Whisper.

- **Imaginea avatarului:**  
  O imagine statică de tip portret (de exemplu, un fișier PNG/JPG) ce va fi folosită de SadTalker.

- **Raspunsul textual generat de LLM:**  
  Textul generat de modelul de limbaj va constitui baza pentru sinteza vocala.

- **Fisierul audio generat:**
  Rezultatul conversiei prin Whisper.
  Audio-ul rezultat va fi sincronizat cu imaginea avatarului pentru a crea un scurt videoclip animat.
 

---

## 4. Fluxul de procesare

1. **Utilizatorul introduce intrebarea textuala.**
2. **Modelul LLM proceseaza intrebarea si genereaza un raspuns textual.**
3. **Sistemul selecteaza avatarul generat de noi.**
4. **Sinteza vocala converteste raspunsul textual in fisier audio.**
5. **Sistemul sincronizeaza fisierul audio cu imaginea avatarului, generand videoclipul final.**

---

## 5. Extensibilitate si dezvoltari viitoare

Structura modulara permite adaugarea rapida a unor functionalitati suplimentare, precum:
- **Antrenare noastra a unui model pentru a raspunde la intrebari**
- **Integrarea a mai multor personaje** 

---

## 6. Resurse utile

- **model SadTalker** (se pun in /checkpoints)
https://drive.google.com/file/d/1gwWh45pF7aelNP_P78uDJL8Sycep-K7j/view

---

## 7. Teaser video
https://youtu.be/L4ErvP6P95w
