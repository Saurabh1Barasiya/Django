# I have created this file.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index1.html',{'placeholder':'Enter your text here'})



def remove_punction(request):
    get_text = request.GET.get('text','defult')
    removepunc = request.GET.get('removepunc','off')
    Capatilize = request.GET.get('Capatilize','off')
    new_line_removal = request.GET.get('new_line_removal','off')
    extra_space_removal = request.GET.get('extra_space_removal','off')
    char_count = request.GET.get('char_count','off')
    
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    if removepunc == 'on' and Capatilize == 'on' and new_line_removal == 'on' and extra_space_removal == 'on' and char_count == 'on':
            text = ""
            for char in get_text:
                if char not in punctuation:
                    text =  text + char 
            uppercase = text.upper()  

            analyze = ''
            for index , value in enumerate(uppercase):                        
                if  uppercase[index] == '' and  uppercase[index+1] == '':
                    pass   
                else:
                    analyze = analyze + value 
            
            count = len(analyze)
            return render(request,'punch2.html',{'text':analyze,'placeholder':'Analyzing','count':count})

    
    elif removepunc == 'on':
        text = ""
        for char in get_text:
            if char not in punctuation:
                text =  text + char 
        print(" Your text here --- >",text) 
        param = {'text':text,'placeholder':'Removeing punctuation'}
        return render(request,'punch1.html',param)

    elif Capatilize == 'on':
        uppercase = get_text.upper()   
        return render(request,'punch1.html',{'text':uppercase,'placeholder':'Change to uppercase'})

    elif new_line_removal == 'on':
        removal = get_text.replace('\n',' ')
        return render(request,'punch1.html',{'text':removal,'placeholder':'Removal new line'})

    elif extra_space_removal == 'on':
        analyze = ''
        for index , value in enumerate(get_text):                        
            if  get_text[index] == ' ' and get_text[index+1] == ' ':
                pass   
            else:
                analyze = analyze + value 
        return render(request,'punch1.html',{'text':analyze,'placeholder':'Removal Extra Space'})
    
    elif char_count == 'on': 
        count = len(get_text) 
        return render(request,'punch1.html',{'text':count,'placeholder':'Total count'})

    

    else:
        return render(request,'punch1.html',{'placeholder':'something went wrong'})


    
# def removepunc(request):
#     text =  request.GET.get('text','defult')
#     removepunction = request.GET.get('removepunc','off')  
#     upper_text = request.GET.get('Capatilize','off')       
#     new_line_removal = request.GET.get('new_line_removal','off')       
#     extra_space_removal = request.GET.get('extra_space_removal','off')       
#     char_count = request.GET.get('char_count','off')       
#     analyze = ""
#     punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
#     if removepunction == 'on':
#         print("if ke ander")
#         for char in text:
#             if char not in punctuation:
#                 analyze =  analyze + char  
#         param = {'analyze':analyze,'placeholder':'Removeing punctuation'}
#         return render(request,'punch1.html',param)
#     elif upper_text == 'on':
#         uppercase = text.upper()   
#         return render(request,'punch1.html',{'text':uppercase,'placeholder':'Change to uppercase'})

#     elif new_line_removal == 'on':
#         removal = text.replace('\n',' ')
#         return render(request,'punch1.html',{'text':removal,'placeholder':'Removal new line'})

#     elif extra_space_removal == 'on':
#         analyze = ''
#         for index , value in enumerate(text):                        
#             if  text[index] == ' ' and text[index+1] == ' ':
#                 pass   
#             else:
#                 analyze = analyze + value 
#         return render(request,'punch1.html',{'text':analyze,'placeholder':'Removal Extra Space'})

#     elif char_count == 'on': 
#         count = len(text) 
#         return render(request,'punch1.html',{'text':count,'placeholder':'Total count'})

#     else:
#         return render(request,'punch1.html',{'text':"Error in input"})

    


