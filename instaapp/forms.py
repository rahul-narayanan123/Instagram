from django import forms
from.models import Profile,Post,Comment


class ProfileForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=['phone','bio','image','name']

class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=['image','description','user','name'] 

        widgets={
             
            'image':forms.FileInput(attrs={'class':'images'}),
            'description':forms.TextInput(attrs={'class':'discrip',}),
            # 'user':forms.TextInput(attrs={'id':'ab',}),
            'name':forms.TextInput(attrs={'class':'names','placeholder':'name'}),


        }  



class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=['comment']  

        widgets={
            'comment':forms.TextInput(attrs={'class':'comment','placeholder':'comment'}),              
        }
     


