from django import forms
from .models import Deck, FlashCard, Tag


class DeckForm(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=100, required=True)
    description = forms.CharField(label="Description", max_length=250, required=False)

    class Meta:
        model = Deck
        fields = "__all__"


class FlashCardForm(forms.ModelForm):
    front = forms.Textarea()
    back = forms.Textarea()
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    decks = forms.ModelMultipleChoiceField(queryset=Deck.objects.all())
    is_question = forms.CheckboxInput()

    class Meta:
        model = FlashCard
        fields = "__all__"
