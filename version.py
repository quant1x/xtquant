from git import Repo
repo = Repo(r'./')
tags = []
for __tag in repo.tags:
    tag = str(__tag)
    tag = tag[1:]
    tags.append(tag)
tags.sort(key=lambda x:tuple(int(v) for v in x.split('.')))
latest = tags[-1]
print(latest)
last_vs = tags[-1].split('.')
last_vs[-1] = str(int(last_vs[-1])+1)
print('.'.join(last_vs))
