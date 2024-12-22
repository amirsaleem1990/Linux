#!/home/amir/.venv_base/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_clipboard()
d1 = {'Ready for review': 1,
     'In Review' : 1,
     '1st Review - Comments Added' : 1,
     '1st Review - Comments addressed' : 1,
     '1st Review - Done' : 2,
     'In 2nd Review' : 2,
     '2nd Review - Comments Addressed' : 2,
     '2nd Review - Comments Added': 2,
     '2nd Review - Done' : 3
}

d2 = {'Ready for review': 0,
     'In Review' : 0,
     '1st Review - Comments Added' : 1,
     '1st Review - Comments addressed' : 1,
     '1st Review - Done' : 2,
     'In 2nd Review' : 2,
     '2nd Review - Comments Addressed' : 2,
     '2nd Review - Comments Added': 2,
     '2nd Review - Done' : 2
}

# Process DataFrame
df = df.loc[:, ['Rater/Evaluator', 'First reviewer', 'Status']]
df = df.dropna()
df['score_1'] = df.Status.map(d1)
df['score_2'] = df.Status.map(d2)
x = df.groupby('Rater/Evaluator').score_1.mean()
y = df.groupby('First reviewer').score_2.mean()

z = (
    x.reset_index()
    .merge(
        y.reset_index(), 
        left_on="Rater/Evaluator", 
        right_on="First reviewer", 
        how="outer"
    )
)
z['IC'] = z['First reviewer'].fillna(z['Rater/Evaluator'])
z = z[['IC', 'score_1', 'score_2']]
z['total'] = z.score_1.add(z.score_2, fill_value=0)
z = z.fillna(0)

z = z.merge(
    df['Rater/Evaluator'].value_counts().rename("Count_Rater").rename_axis("IC").to_frame().merge(
        df['First reviewer'].value_counts().rename("Count_First_Reviewer").rename_axis("IC").to_frame(),
        how='outer', left_index=True, right_index=True
    ).reset_index(), on="IC"
)

my_score = z.loc[z.IC.eq("amir.s@turing.com"), "total"].iloc[0]

print("My score  :", my_score)
print("Avg. score:", z.total.mean())
print(z.total.le(my_score).mean())
print()
print(z.sort_values(by='total', ascending=False).to_markdown())
print()
print(df.to_markdown(index=False))
print()

z.IC = z.IC.replace("amir.s@turing.com", "AAAAAAAAAAAA")
z = z.sort_values(by=['total', 'IC'], ascending=[True, False])
z.IC = z.IC.replace("AAAAAAAAAAAA", "amir.s@turing.com")
z = z.reset_index(drop=True)
# print(z.to_markdown())
# exit()

# Bar plot with custom color for "Amir"
z = z.set_index("IC")
colors = ['red' if index == 'amir.s@turing.com' else 'blue' for index, _ in z.iterrows()]
z.total.plot(kind='barh', color=colors)
plt.show()

# Box plot with horizontal line at your score
z.total.plot(kind='box')
plt.axhline(my_score, color='red', linestyle='--')
plt.show()
