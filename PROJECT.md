# Sistem Conversational Interactiv cu Avatar Animat

---

##  Definirea problemei

**Scopul proiectului:**

Dezvoltarea unui sistem conversațional interactiv care răspunde vocal la întrebările utilizatorului folosind un avatar animat.

**Problema abordată:**

Lipsa interacțiunii naturale în sistemele clasice de răspuns automat.

**Input:**
- Întrebare textuală de la utilizator
- Imagine avatar (generată)

**Output:**
- Răspuns vocal + video animat al avatarului care răspunde

---

##  Analiza datelor de intrare

- Textul introdus de utilizator (input liber, limbaj natural)
- Imaginea avatarului generată cu DALL-E 3
- Răspunsul textual generat de GPT-4.1
- Audio generat cu libraria: whisper
- Toate sunt integrate pentru a produce un videoclip sincronizat (audio-video).

---

## Model AI folosit și dezvoltare

**Model AI folosit:**
- LLM-UL GPT-4.1 pentru răspunsuri 
- Text-to-Speech pentru voce naturală 
- Model de animație facială (SadTalker)

**Evaluarea performanței:**
- Calitatea răspunsurilor LLM este foarte calitativa, datorita utilizarii modelului GPT-4.1
- Realismul sincronizării video/audio, avatarul vorbeste perfect peste fisierul audio, <br> gesturile faciale potrivindu-se si sincronizandu-se cu audio-ul

---

##  Îmbunătățiri posibile

- Înlocuirea imaginii statice cu un avatar 3D în timp real
- Răspunsuri personalizate în funcție de contextul utilizatorului
- Detectarea tonului vocii și ajustarea expresiilor faciale
- Integrarea mai multor limbi
- Adaugarea de mai multe personaje

---

##  Teaser video

** https://youtu.be/L4ErvP6P95w **

**Descriere teaser:**

Utilizatorul întreabă: "Tell me something about U.B.B.?"

Avatarul răspunde vocal

Avatarul clipește și mișcă buzele sincron cu vocea.

---

## Tehnologii folosite

- GPT-4.1 / ChatGPT (LLM)
- DALL·E 3 (generare avatar)
- SadTalker (animație video sincronizată)
- Whisper (generare audio)

---

##  Impact asupra Obiectivelor de Dezvoltare Durabilă (SDG)

**SDG 4 - Educație de calitate**
- Facilitează învățarea interactivă prin avatar inteligent

**SDG 10 - Reducerea inegalităților**
- Poate fi folosit pentru accesibilitate: ghidare vocală pentru persoane cu dizabilități

**Motivație:**
- Oferă acces la informații într-o formă naturală și prietenoasă, inclusiv celor cu dificultăți de lectură sau învățare

---

##  Concluzie

- Proiectul aduce un plus major în experiența interacțiunii om-calculator
- Integrează AI modern într-un mod prietenos și accesibil
- Poate fi extins în educație, customer service, sănătate, etc.

**Vă mulțumesc!**
