from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    if request.method == "POST":
        text=request.POST["data"]
        lines=list(text.split("\n"))
        print(lines)
        k=0
        for line in lines:
            li=list(line.split())
            k+=len(li)
        dic={"dic":k}
        return render(request,"home.html",dic)
    return render(request,"home.html")


    