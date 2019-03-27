from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import View

import spacy
import random

def index(request):
     return render(request,'quest/index.html')

def get(request):
     person_type = ["archaeologist", "farmer", "hunter", "hunter gatherer", "shopkeeper", "wholesaler",
                    "wandering herder"]
     animal = ["dog", "sheep", "goat", "cow", "pig", "deer"]
     tools = ["grinding stone", "flour", "pot", "utensil", "medal", "knife", "hand axe", "needles", "money"]
     years = ["12000", "4,500", "3,500", "1200", "3,200", "5,000"]
     animal_type = ["wild", "domestic"]
     place = ["west asia", "southeast asia", "mekong delta", "europe", "satpura", "vindhya", "central india",
              "bhimbetka", "andaman and nicobar islands"]
     state = ["madhya pradesh"]
     age = ["stone age", "metal age", "copper age", "bronze age", "paleolithic age", "mesolithic age", "neolithic age"]
     metal = ["copper", "bronze", "tin", "iron"]
     country = ["india", "egypt", "china", "turkey", "england", "germany", "united states"]
     work = ["hunt", "fish", "persistence hunt", "trade", " shipbuild"]
     names = ["marco polo", "christopher columbus", "vasco da gama", "ferdinand magellan"]
     century = ["17th", "18th", "19th", "20th", "21st"]
     invention = ["car", "flight", "wheel", "locomotive", "electricity"]
     comm = ["printing press", "telephone", "telegraph", "typewriter", "radio", "television", "satellite", "internet",
             "mobile phone"]
     # Civics
     calledc = ["democracy", "directive", "constituency", "political party", "opposition"]
     rights = ["equality", "freedom", "education", "religion", "live"]
     systems = ["legislature", "executive", "judiciary", "constituency", "constitution"]
     posts = ["president", "governor", "prime minister", "chief minister", "mp", "mla"]
     courts = ["high court", "supreme court", "district court", "normal court", "tennis court"]
     sabha = ["parliament", "vidhan sabha", "rajya sabha", "legislative assembly", "lok sabha"]
     # Geography
     calledg = ["latitude", "longitude", "hemisphere", "meridian", "equator", "altitude"]
     direc = ["east", "west", "north", "south", "southeast"]
     direc2 = ["northeast", "northwest", "southeast", "southwest", "east"]
     ctr = ["jakarta", "new york", "africa", "india", 'USA']
     clm_type = ["hot", "humid", "pleasant", "cold", "temperate"]
     clm_2 = ["winter", "summer", "monsoon", "spring", "rainy"]
     global ques
     ques = ""
     if request.method=='POST':
          add_data = request.POST.copy()
          txt = add_data.get("text")
          nlp = spacy.load('en_coref_md')
          nlp1 = spacy.load('en_core_web_md')
          if 'MCQS' in request.POST:
               cnt=1
               doc = nlp1(txt)
               dictn = [person_type, animal, tools, years, animal_type, place, age, metal, country, work, names,
                        century, invention, comm, calledc, rights, systems, posts, courts, sabha, calledg, direc,
                        direc2, ctr, clm_type, clm_2]
               # print(text1)
               list99 = list(doc.sents)
               # print(list99)
               list98 = []
               # for j in range(len(list99)):
               # if list99[j].isupper():
               # print(list99)
               list98 = []
               ll = 1
               for j in range(len(list99)):
                    if str(list99[j]).isupper():
                         ll = 1
                    else:
                         list98.append(list99[j])



               for line9 in list98:
                    txt1 = str(line9)
                    nounsinsent = []
                    tk = ""
                    for token in line9:
                         # print(token.text,token.tag_,token.lemma_)
                         if "NN" in str(token.tag_):
                              nounsinsent.append(str(token.lemma_).lower())
                              txt1 = txt1.replace(str(token.text), str(token.lemma_).lower())
                              tk = tk + str(token.lemma_).lower() + " "
                         else:
                              if tk != "":
                                   tk = tk[0:(len(tk) - 1)]
                              if " " in tk:
                                   nounsinsent.append(tk)
                              tk = ""
                              # print(nounsinsent)
                    for nouns in nounsinsent:
                         fl = 0
                         for x in dictn:
                              j = 0
                              # print("x=",x)
                              for y in x:
                                   # print("y=",y)
                                   if y == nouns:
                                        fl = 1
                                        break
                                   j = j + 1
                              if fl == 1:
                                   z = x
                                   break
                         if fl == 1:
                              # print(nouns)
                              ans = txt1.replace(nouns, "________")
                              m = len(z)
                              # print(ans)
                              ques = ques +str(cnt)+"."+ ans + "\n"
                              cnt=cnt+1
                              # print(ques)
                              number1 = random.randrange(0, 4)
                              # print(number1)
                              # print(notin,j)
                              notin = [j]
                              i = 0
                              while i < 4:
                                   number = random.randrange(0, m)
                                   if number in notin:
                                        # print(number)
                                        i = i - 1
                                   else:
                                        if i == number1:
                                             # print(i+1,".",nouns)
                                             ques = ques + str(i + 1) + "." + str(nouns) + "\n"
                                        else:
                                             # print(i+1,".",z[number])
                                             ques = ques + str(i + 1) + "." + str(z[number]) + "\n"
                                             notin.append(number)
                                   i = i + 1
                              # print()
                              ques = ques + "\n"
                              # print("Correct answer:",nouns)
                              ques = ques + "Correct answer: " + str(nouns) + "\n"
                              # print()
                              ques = ques + "\n"
                              # print()
                              ques = ques + "\n"
                              break

               #print(ques)
          if 'WH' in request.POST:
               doc = nlp(txt)
               list1 = list(doc.sents)
               c = -1
               k = 1
               ans = ""
               for x in list1:
                    line = str(x)
                    # print(line)
                    line09 = nlp1(line)
                    cnt = 0
                    cnta = 0
                    cntb = 0
                    cntc = 0
                    cntd = 0
                    c = c + 1
                    if ":" in line:
                         l = line.split(':')
                         m = nlp(l[0])
                         for token in m:
                              if (token.tag_ == "VBP"):
                                   b = str(token.text)
                                   n = str(m).split(b)
                                   ques = str(k) + ") " + "What " + b + " " + n[0].lower() + n[1] + '?'
                                   q = nlp(ques)
                                   for t in q:
                                        if str(t.tag_) == "NN":
                                             b = 1
                                             break
                                   if b == 1:
                                        # print(str(k)+") "+ques)
                                        ans = ans + str(k) + ") " + ques + '\n'
                                        k = k + 1
                                        break
                    elif "when" in line:
                         l = line.split('when')
                         line1 = nlp1(str(l[0]))
                         print(str(l[0]))
                         h = ""
                         for token in line1:
                              # print(token.text,token.dep_)
                              if "aux" in str(token.dep_):
                                   h = h + token.text
                                   break
                         if h != "":
                              m = str(line1).split(h)
                              ques = 'When' + ' ' + h + ' ' + m[0].lower() + m[1] + '?'
                         else:
                              ques = 'When' + ' ' + str(line1) + '?'
                         # print(str(k)+") "+ques)
                         ans = ans + str(k) + ") " + ques + '\n'
                         k = k + 1
                    elif "because" in line.lower():
                         l = line.lower().split('because')
                         line1 = nlp1(str(l[0]))
                         h = ""
                         if str(l[0]) == " ":
                              l1 = line.split(',')
                              m = nlp1(str(l1[1]))
                              for token in m:
                                   if str(token.tag_) == "DT":
                                        n = str(m).split(str(token.text))
                                        n[1] = n[1].replace(n[1][-1], '?')
                                        ques = "Which" + "" + n[1].lower()
                                        # print(str(k)+") "+ques)
                                        ans = ans + str(k) + ") " + ques + '\n'
                                        k = k + 1
                         else:
                              for token in line1:
                                   # print(token.text,token.dep_,token.tag_)
                                   if "aux" in str(token.dep_):
                                        h = h + token.text
                                        break
                                   if h != "":
                                        m = str(line1).split(h)
                                        ques = 'Why' + ' ' + h + ' ' + m[0].lower() + m[1] + '?'
                                   else:
                                        ques = 'Why' + ' ' + str(line1).lower() + '?'
                                   q = nlp(ques)
                                   for t in q:
                                        if str(t.tag_) == "NN":
                                             b = 1
                                             break
                                   if b == 1:
                                        # print(str(k)+") "+ques)
                                        ans = ans + str(k) + ") " + ques + '\n'
                                        k = k + 1
                                   break
                    elif "called" in line:
                         b = 0
                         l = line.split('called')
                         m = nlp(l[0])
                         for token in m:
                              ques = 'What' + " " + str(m[-1:]) + " " + str(m[:-1]).lower() + " called ?"
                              q = nlp(ques)
                              for t in q:
                                   if str(t.tag_) == "NN":
                                        b = 1
                                        break
                              if b == 1:
                                   # print(str(k)+") "+ques)+'\n'
                                   ans = ans + str(k) + ") " + ques + '\n'
                                   k = k + 1
                              break
                    elif "As a result" in line:
                         l = line.split('As a result,')
                         m = nlp(l[1])
                         h = ""
                         for token in m:
                              # print(token.text,token.dep_,token.tag_)
                              if "aux" in str(token.dep_):
                                   h = h + token.text
                                   break
                         if h != "":
                              n = str(m).split(h)
                              p = n[1]
                              ques = 'Why' + ' ' + h + ' ' + n[0].lower() + p[:-1] + '?'
                              # print(str(k)+") "+ques)
                              ans = ans + str(k) + ") " + ques + '\n'
                         else:
                              for token in m:
                                   if (token.tag_ == "VBP"):
                                        a = "do"
                                   elif (token.tag_ == "VBD"):
                                        a = "did"
                                   elif (token.tag_ == "VBZ"):
                                        a = "does"
                         n = str(m)
                         for token in m:
                              if (token.tag_ == "VBD" or token.tag_ == "VBP" or token.tag_ == "VBZ"):
                                   n = re.sub(str(token.text), str(token.lemma_), n)
                         ques = 'Why' + ' ' + a + ' ' + n.lower() + '?'
                         # print(str(k)+") "+ques)
                         ans = ans + str(k) + ") " + ques + '\n'
                         k = k + 1
                         break
                    elif "for example" in line.lower() or "for instance" in line.lower():
                         if "for example" in line.lower():
                              b = "for example"
                         else:
                              b = "for instance"
                         l = line.lower().split(b)
                         if not l[0]:
                              ques = 'Give an example:' + ' ' + str(list1[c - 1]).lower()
                         else:
                              if "-" in str(l[0]).lower():
                                   l = str(l[0]).lower().split('-')
                                   ques = 'Give an example:' + ' ' + str(l[1]).lower()
                              else:
                                   ques = 'Give an example:' + ' ' + str(l[0]).lower()
                              if ques[-1] == ",":
                                   ques = ques.replace(ques[-1], '.')
                         # print(str(k)+") "+ques)
                         ans = ans + str(k) + ") " + ques + '\n'
                         k = k + 1
                    elif "since" in line:
                         z = 0
                         l = line.split('since')
                         line1 = nlp1(str(l[0]))
                         line3 = nlp1(str(l[1]))
                         for ent in line3.ents:
                              if str(ent.label_) == 'TIME' or str(ent.label_) == 'DATE':
                                   z = 1
                                   break
                         for token in line3:
                              if str(token.lemma_) == 'start' or str(token.lemma_) == 'end' or str(
                                      token.lemma_) == 'begin':
                                   z = 1
                                   break
                         h = ""
                         for token in line1:
                              # print(token.text,token.dep_)
                              if "aux" in str(token.dep_):
                                   h = h + token.text
                                   break
                         if z == 0:
                              if h != "":
                                   m = str(line1).split(h)
                                   ques = 'Why' + ' ' + h + ' ' + m[0].lower() + m[1] + '?'
                              else:
                                   line2 = str(line1)
                                   line2 = line2.replace(line2[-1], " ")
                                   ques = 'Why' + ' ' + line2.lower() + '?'
                         else:
                              if h != "":
                                   m = str(line1).split(h)
                                   ques = 'Since when' + ' ' + h + ' ' + m[0].lower() + m[1] + '?'
                              else:
                                   ques = 'Since when' + ' ' + str(line1) + '?'
                         # print(str(k)+") "+ques)
                         ans = ans + str(k) + ") " + ques + '\n'
                         k = k + 1
                    elif "hence" in line.lower() or "thus" in line.lower() or "therefore" in line.lower():
                         if "hence" in line.lower():
                              l = (line.lower()).split('hence')
                         elif "thus" in line.lower():
                              l = (line.lower()).split('thus')
                         elif "therefore" in line.lower():
                              l = (line.lower()).split('therefore')
                         ques = 'Explain why' + ' ' + str(l[1]) + '?'
                         # print(str(k)+") "+ques)
                         ans = ans + str(k) + ") " + ques + '\n'
                         k = k + 1
                    elif "although" in line or "though" in line or "however" in line:
                         if "although" in line:
                              l = line.split('although')
                         elif "though" in line:
                              l = line.split('though')
                         else:
                              l = line.split('however')
                         line100 = nlp1(line)
                         for token in line100:
                              # print(token.text,token.dep_,token.tag_)
                              line1 = nlp1(str(l[1]))
                              line2 = nlp1(str(l[0]))
                         h = ""
                         for token in line1:
                              # print(token.text,token.dep_,token.tag_)
                              if "aux" in str(token.dep_):
                                   h = h + token.text
                                   break
                         if h != "":
                              m = str(line1).split(h)
                              p = m[1]
                              ques = h.capitalize() + ' ' + m[0].lower() + p[:-1] + '?'
                              # print(str(k)+") "+ques)
                              ans = ans + str(k) + ") " + ques + '\n'
                              k = k + 1
                              h1 = h + '\'t'
                              ques = h1.capitalize() + ' ' + m[0].lower() + p[:-1] + '?'
                              # print(str(k)+") "+ques)
                              ans = ans + str(k) + ") " + ques + '\n'
                              k = k + 1
                         # print(str(k)+") "+ques)
                         ans = ans + str(k) + ") " + ques + '\n'
                         k = k + 1
                         break
                    elif "-" in line:
                         l = line.split('-')
                         m = nlp(l[0])
                         if str((l[1][:1]).isupper()) == "True":
                              for token in m:
                                   if str(token.tag_) == "-RRB-":
                                        h = token.text
                                        l[0] = str(m).split(h)
                                        m = l[0][1]
                                   ques = "Write in detail about " + str(m).lower() + "?"
                              # print(str(k)+") "+ques)
                              ans = ans + str(k) + ") " + ques + '\n'
                              k = k + 1
                    elif str(line.isupper()) == "True" and "SUMMARY" not in line:
                         b = 0
                         ques = "Write short note on " + line.lower()
                         ques = nlp(ques)
                         for token in ques:
                              if (str(token.tag_) == "-RRB-"):
                                   b = 1
                                   break
                         if b == 0:
                              # print(str(k)+") "+str(ques))
                              ans = ans + str(k) + ") " + str(ques) + '\n'
                              k = k + 1
               ques=ans
          if 'FIB' in request.POST:
               doc = nlp(txt)
               list1 = list(doc.sents)
               ans = ""
               c = -1
               k=1
               for x in list1:
                    line = str(x)
                    line09 = nlp(line)
                    c = c + 1
                    if "means" in line:
                         l = line.split('means')
                         m = nlp(l[1])
                         for token in m:
                              ques = "______ means" + str(m)
                              # print(str(k)+") "+ques)
                              ans = ans + str(k) + ") " + ques + '\n'
                              k = k + 1
                              break
                    elif "called" in line:
                         b = 0
                         l = line.split("called")
                         m = nlp(l[0])
                         for token in m:
                              ques = str(m) + " called______."
                              ques = nlp(ques)
                         for token in ques:
                              if str(token.tag_) == 'NN' or str(token.tag_) == 'JJ':
                                   b = 1
                                   break
                         if b == 1:
                              # print(str(k)+") "+str(ques))
                              ans = ans + str(k) + ") " + str(ques) + '\n'
                              k = k + 1
                    for e in line09.ents:
                         if str(e.label_) == 'LAW':
                              line = line.replace(e.text, "________")
                              # print(str(k)+") "+line)
                              for token in nlp(line):
                                   if str(token.text) == "this" or str(token.text) == "these" or str(
                                           token.text) == "that":
                                        line = str(list1[c - 1]) + line
                              # print(str(k)+") "+line)
                              ans = ans + str(k) + ") " + line + '\n'
                              k = k + 1
                              break
                         elif str(e.label_) == 'DATE':
                              line = line.replace(e.text, "________")
                              # print(str(k)+") "+line)
                              for token in nlp(line):
                                   if str(token.text).lower() == "this" or str(token.text).lower() == "these" or str(
                                           token.text).lower() == "that":
                                        line = str(list1[c - 1]) + line
                              # print(str(k)+") "+line)
                              ans = ans + str(k) + ") " + line + '\n'
                              k = k + 1
                              break
               #print(ans)
               ques=ans





          return render(request,'quest/question.html',{'ques':ques})


