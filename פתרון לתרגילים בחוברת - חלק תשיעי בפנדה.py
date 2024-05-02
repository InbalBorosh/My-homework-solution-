import pandas as pd
import matplotlib.pyplot as plt
import os
os.getcwd()
os.chdir(r'C:\Users\PC\Desktop\data analist\python')

categories = pd.read_excel('categories.xlsx')
products = pd.read_excel('Product.xlsx')
categories.head(5)
products.head(5)
products.columns
categories.columns

pd.merge(products, categories, how= 'left', on= 'CategoryID').head(5)
mrg = pd.merge(products, categories, how= 'left', on= 'CategoryID')
mask = mrg.groupby('CategoryName')['UnitPrice'].mean().sort_values(ascending= False)
mask.index
#print(mask)

y = mask
x = mask.index
plt.barh(x, y, color= 'c', label='Avg Price')
plt.xlabel('Average')
plt.ylabel('Category Name')
plt.title('Average Price By Category')
plt.legend(loc= 'upper right')


y = mask
x = mask.index
plt.bar(x, y, color= 'c', label='Avg Price')
plt.ylabel('Average')
plt.xlabel('Category Name')
plt.xticks(fontsize= 6)
plt.xticks(rotation = 50)
plt.title('Average Price By Category')
plt.legend(loc= 'upper right')


y = mask
x = mask.index
plt.pie(y, labels= x, shadow=True, explode= [0.2, 0, 0, 0, 0, 0, 0, 0], autopct='%1.2f%%', radius= 2)
#plt.ylabel('Average')
plt.title('Average Price By Category')
plt.style.use('seaborn-v0_8 Style')


y = mask
x = mask.index
plt.pie(y, labels= x, shadow=True, explode= [0.2, 0, 0, 0, 0, 0, 0, 0], autopct= lambda p:'{:.1f}%({:.0f})'.format(p, p*sum(mask)/100), radius= 2)
#plt.ylabel('Average')
plt.title('Average Price By Category')
plt.style.use('seaborn-v0_8-pastel')
plt.yticks(fontsize= 6)
#print(plt.style.available)


pup = pd.read_excel('pupils.xlsx')
pup.head(5)
Hm = pup[pup['gen'] == 'M'].groupby('Age')['Height'].mean()
Hf = pup[pup['gen'] == 'F'].groupby('Age')['Height'].mean()
Wm = pup[pup['gen'] == 'M'].groupby('Age')['Weight'].mean()
Wf = pup[pup['gen'] == 'F'].groupby('Age')['Weight'].mean()

print(Hm)

# =============================================================================
# plt.plot(Hm.index, Hm)
# plt.plot(Hf.index, Hf)
# plt.plot(Wm.index, Wm)
# plt.plot(Wf.index, Wf)
# =============================================================================

plt.subplot(2, 2, 1)
plt.plot(Hm.index, Hm)
plt.title('Avg Male Height', fontsize=8)
#plt.subplots_adjust(hspace=0.4, top=0.85)

plt.subplot(2, 2, 2)
plt.plot(Hf.index, Hf)
plt.title('Avg Female Height', fontsize=8)

plt.subplot(2, 2, 3)
plt.plot(Wm.index, Wm)
plt.title('Avg Male Weight', fontsize=8)


plt.subplot(2, 2, 4)
plt.plot(Wf.index, Wf)
plt.title('Avg Female Weight', fontsize=8)

# adding space between graphs
plt.subplots_adjust(hspace=0.4, top=0.85)
plt.tight_layout()



fig = plt.figure()

# Needed to add spacing between 1st and 2nd row
# Add a margin between the main title and sub-plots
fig.subplots_adjust(hspace=0.4, top=0.85)

# Add the main title
fig.suptitle("Title 1", fontsize=15)

# Add the subplots
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

# Add the text for each subplot
ax1.plot(Hm.index, Hm)
ax1.title.set_text("Avg Male Height")

ax2.plot(Hf.index, Hf)
ax2.title.set_text("Avg Female Height")

ax3.plot(Wm.index, Wm)
ax3.title.set_text("Avg Male Weight")

ax4.plot(Wf.index, Wf)
ax4.title.set_text("Avg Female Weight")

plt.show()















