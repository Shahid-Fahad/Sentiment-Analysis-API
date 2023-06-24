from django.shortcuts import render,redirect
from django.http import HttpResponse
from setfit import SetFitModel
from django.http import JsonResponse
from django.http import HttpResponseRedirect

# Create your views here.
def f2(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        return redirect('analyze', anatext=text)
    else:
        return render(request, 'home.html')

def res(request,anatext):
        # Initialize and load the SetFit model
        model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
        # Run inference on the input text
        preds = model([anatext])
        # Process the predictions as needed
        sentiment_tensor = preds[0]  # Assuming the model predicts sentiment
        
        #labelling sentiment_tensor for meaningfull outcomes
        sentiment="Neutral"
        if sentiment_tensor==1:
            sentiment="Positive"
        else:
            sentiment="Negative"
        
        # Render the results in a template
        #return redirect('analyze',text)
        return render(request, 'results.html', {'sentiment': sentiment})


