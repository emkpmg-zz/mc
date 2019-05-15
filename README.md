# Edible Mushroom Prediction ( Classification)
This is an ML application to agriculture/health. This binary classification model is expected to classify mushrooms as poisonous or not based on relevant attributes of the mushroom.This dataset has feature description of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family (pp. 500-525). Each species is identified as definitely edible, definitely poisonous, or unknown edibility and not recommended. The unknown class is considered to be part of the poisonous species. 

# Key Mushroom Features
cap-shape: bell=b, conical=c, convex=x, flat=f, knobbed=k, sunken=s
cap-surface: fibrous=f, grooves=g, scaly=y, smooth=s
cap-color: brown=n, buff=b, cinnamon=c, gray=g, green=r, pink=p, purple=u, red=e, white=w, yellow=y
bruises?: bruises=t, no=f
odor: almond=a, anise=l, creosote=c, fishy=y, foul=f, musty=m, none=n, pungent=p, spicy=s
gill-attachment: attached=a, descending=d, free=f, notched=n
gill-spacing: close=c, crowded=w, distant=d
gill-size: broad=b, narrow=n
gill-color: black=k, brown=n, buff=b, chocolate=h, gray=g, green=r, orange=o, pink=p, purple=u, red=e, white=w, yellow=y
stalk-shape: enlarging=e, tapering=t
stalk-root: bulbous=b, club=c, cup=u, equal=e, rhizomorphs=z, rooted=r, missing=?
stalk-surface-above-ring: fibrous=f, scaly=y, silky=k, smooth=s
stalk-surface-below-ring: fibrous=f, scaly=y, silky=k, smooth=s
stalk-color-above-ring: brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y
stalk-color-below-ring: brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y
veil-type: partial=p, universal=u
veil-color: brown=n, orange=o, white=w, yellow=y
ring-number: none=n, one=o, two=t
ring-type: cobwebby=c, evanescent=e, flaring=f, large=l, none=n, pendant=p, sheathing=s, zone=z
spore-print-color: black=k, brown=n, buff=b, chocolate=h, green=r, orange=o, purple=u, white=w, yellow=y
population: abundant=a, clustered=c, numerous=n, scattered=s, several=v, solitary=y
habitat: grasses=g, leaves=l, meadows=m, paths=p, urban=u, waste=w, woods=d

N.B: Mushroom attributes in this dataset are categorical. To enhance efficiency of learning and prediction algorithms, these string descriptions will be converted to numeric or indicator variables.

# Other Details
Dataset Characteristics:    Multivariate
No. of Records:             8124
Area:                       Life
Attribute Characteristics:  Categorical
Number of Attributes:       22
Date Donated:               1987-04-27
Missing Values?             Yes

# DATA SOURCE
Data was aquired from the UCI Mushroom Data Set [http://archive.ics.uci.edu/ml/datasets/Mushroom?ref=datanews.io].

# Origin: 
Mushroom records drawn from The Audubon Society Field Guide to North American Mushrooms (1981). G. H. Lincoff (Pres.), New York: Alfred A. Knopf 
N.B: The Guide clearly states that there is no simple rule for determining the edibility of a mushroom; no rule like; "leaflets three, let it be" for Poisonous Oak and Ivy.

# Donated By: Jeff Schlimmer (Jeffrey.Schlimmer '@' a.gp.cs.cmu.edu)

# Reference
Schlimmer,J.S. (1987). Concept Acquisition Through Representational Adjustment (Technical Report 87-19). Doctoral disseration, Department of Information and Computer Science, University of California, Irvine. 
[http://rexa.info/paper/fbd1dcb58b86c6fa9bb5eadb994213d751a55ff7] 

Iba,W., Wogulis,J., & Langley,P. (1988). Trading off Simplicity and Coverage in Incremental Concept Learning. In Proceedings of the 5th International Conference on Machine Learning, 73-79. Ann Arbor, Michigan: Morgan Kaufmann. 
[http://rexa.info/paper/e5b500eb8d8cc46b19f7ddf4d0876060c4bcf844] 

Duch W, Adamczak R, Grabczewski K (1996) Extraction of logical rules from training data using backpropagation networks, in: Proc. of the The 1st Online Workshop on Soft Computing, 19-30.Aug.1996, pp. 25-30, [http://www.bioele.nuee.nagoya-u.ac.jp/wsc1/] 
[http://rexa.info/paper/41ba321976970401618d6748a9ecbd769bc50da9] 

Duch W, Adamczak R, Grabczewski K, Ishikawa M, Ueda H, Extraction of crisp logical rules using constrained backpropagation networks - comparison of two new approaches, in: Proc. of the European Symposium on Artificial Neural Networks (ESANN'97), Bruge, Belgium 16-18.4.1997. 
[http://rexa.info/paper/cbfc5b79f03770a32505b3342b2e330a1626be7d]

# Publication Citation Reference
http://archive.ics.uci.edu/ml/citation_policy.html

