from django.shortcuts import render
from django.http import HttpResponse
from hollywood.models import Movie, Actor

def genres(request):
    mv = Movie.objects.all()
    ls=[]
    all_rate=[]
    for i in mv:
        try:
            all_rate.append([i.genre,float(i.imdb_rating)])
        except:
            pass
        g=i.genre.split(',')
        for x in g:
            ls.append(x)
    all_genre=set(ls)
    dc={}
    rate=[]
    rez=''
    for i in all_genre:
        got=[]
        dc[i]=ls.count(i)
        
        for x in all_rate:
            if i in x[0]:
                got.append(x[1])
        rate.append(format(sum(got)/len(got), '.3g'))
        rez=rez+'<p>Жанр: '+i+'\nКол. фильмов: '+str(ls.count(i))+'\nСредний рейтинг: '+str(format(sum(got)/len(got), '.3g')+'</p>')
    return HttpResponse(str(rez))

def actors(request):
    mv = Movie.objects.all()
    ls=[]
    all_rate=[]
    for i in mv:
        g=i.genre.split(',')
        
        for x in g:
            try:
                all_rate.append([x,float(i.imdb_rating)])
            except Exception as e:
                print(e)
            ls.append(x)
    all_genre=set(ls)
    dc={}
    for ge in all_rate:
        if ge[0] in dc:
            got=dc[ge[0]]
            dc[ge[0]]=(got+ge[1])/2
        else:
            dc[ge[0]]=ge[1]
            
    ac = Actor.objects.all()[:20]
    actors=''
    for i in ac:
        ge=[]
        mv = Movie.objects.filter(actors__id=i.actor_id)
        for x in mv:
            g=x.genre.split(',')
            for y in g:
                ge.append(y)
        ge=set(ge)
        got_ge=[]
        for x in ge:
            if not got_ge:
                got_ge=[x,dc[x]]
            elif got_ge[1]<dc[x]:
                got_ge=[x,dc[x]]
        actors+='<p>'+i.name+' '+str(len(mv))+' '+str(got_ge)+'</p>'
    return HttpResponse(str(actors))


def directors(request):
    mv = Movie.objects.all()[:20]
    ls=[]
    rez=''
    for i in mv:
        act=[]
        actor_rate=[]
        act_rate=[]
        mv_rate=[]
        dc={}
        if i.director!='N/A':
            all_mv = Movie.objects.filter(director=i.director)
            ls.append(i.director)
            dire=i.director
            for x in all_mv:
                mv_rate.append([x.title,x.imdb_rating])
                for y in x.actors_names.split(', '):
                    act.append(y)
            for z in set(act):
                act_rate.append([z,act.count(z)])
#            {“name”: “Anna Smith”, “movie_count”: 1}
            act_rate.sort(key=lambda st: int(st[1]),reverse=True)
            for i in act_rate[:3]:
                dc['name']=i[0]
                dc['movie_count']=i[1]
                actor_rate.append(dc)
                dc={}
            mv_rate.sort(key=lambda st: int(st[1]),reverse=True)
            ls.append(actor_rate)
            rez+='<p>'+dire+'</p><p>'+str(actor_rate)+'</p><p>'+str(mv_rate[:3])+'</p>'
    return HttpResponse(str(rez))









