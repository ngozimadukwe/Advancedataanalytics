
# coding: utf-8

# In[1]:


text='''A CerTaiN kING HaD a bEaUtIFul gaRDEn, ANd IN THe GarDen StooD A trEe
whICH bORe GoLDeN ApPlEs. THesE aPples WerE alwAyS CoUntEd, aNd abOuT
tHE TiMe WheN tHEY BEgAn tO grow RipE IT wAs foUND THat EVeRY NIgHT ONE
OF THeM Was gOne. thE kiNg bECAMe veRy ANGRy at thiS, aND ORDEred the
GarDEneR TO KEeP WAtch ALL NIgHT uNDER the tREE. tHE gardener sEt hIs
ELdEsT SoN to WATCH; buT ABout TweLve O’clOCK He fELL ASlEEp, And in
the morNIng aNOTheR Of thE aPPLes Was mIssinG. tHEn THE sECONd Son waS
oRdERED to waTch; aNd AT mIDniGhT he tOO FELl ASleEP, aND iN thE mOrNIng
ANoThER AppLE WaS gOne . TheN THe thIrd Son oFfeREd tO KeEp wATCh; buT
thE garDENer At First WoULd NoT LET Him, FOr fEaR sOMe HArM ShOuLD cOME
To hIM: hoWeveR, at lAST hE coNSEnteD, AND tHE YouNg MAN laID HimSELf
uNDER tHE tREe TO wAtch. AS tHE clocK STRuCk tweLvE He Heard A rustlinG
NoISe IN ThE aIr, And a biRd CAME FlYing ThAt was Of PUre gOLd; AND as
IT WAs SNApPING At onE oF ThE aPpleS wIth iTS BeaK, tHE GArDEner’S son
jUMpED UP And SHOT AN aRrOw at iT. But THE arrOw DID thE BiRD nO HaRm;
ONlY iT dRoPPEd a GoLDEn FEather FROM iTS tAiL, aND THEN FLEw AwaY.
the gOLdEN FEAthER WAS bRoUght to THe KinG IN THE MOrNING, AnD aLL ThE
cOunCil WAs called TogETHER. EVERYoNE aGREed ThAt it wAS wORth MoRe THAn
aLl The weAltH Of tHE kIngDOm: But THE KiNg sAID, ‘One FeatHeR Is Of NO
use tO me, I MusT HaVE ThE wHOLE BIRD .’

'''


# In[2]:


print(text)


# In[3]:


for char in "'-,;:\n.’":
    text=text.replace(char,'')


# In[4]:


print(text)


# In[5]:


text = text.lower()


# In[6]:


textlist = text.split()


# In[7]:


print (textlist)


# In[8]:


from collections import Counter
Counter(textlist).most_common()


# In[10]:


print("there are {} words".format(len(textlist)))

