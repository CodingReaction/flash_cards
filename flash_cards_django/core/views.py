from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpRequest

from .forms import DeckForm, FlashCardForm
from .models import Deck, FlashCard


def index(request: HttpRequest):
    decks = Deck.objects.all()
    return render(request, 'core/index.html', {"decks": decks})


def deck_create(request: HttpRequest,):
    if request.method == "POST":
        deck_form = DeckForm(request.POST)
        if deck_form.is_valid():
            new_deck_data = deck_form.save()
            return redirect(reverse("core:deck-edit", args=[new_deck_data.id]))
    # if GET request or invalid form
    deck_form = DeckForm()
    return render(request, 'core/deck/create.html', {"deck_form": deck_form})


def deck_edit(request: HttpRequest, id: int):
    if request.method == "POST":
        deck_form = DeckForm(request.POST)
        if deck_form.is_valid():
            deck_form.save()
            return redirect(reverse('core:index'))
    deck = get_object_or_404(Deck, pk=id)
    deck_form = DeckForm(instance=deck)
    flash_cards = FlashCard.objects.filter(decks__pk=id)
    context = {
        "deck_form": deck_form,
        "deck": deck,
        "flash_cards": flash_cards}

    return render(request, 'core/deck/edit.html', context)


def card_create(request: HttpRequest):
    deck_id = request.GET.get("deck", None)
    if request.method == "POST":
        card_form = FlashCardForm(request.POST)
        if card_form.is_valid():
            card_form.save()
            if deck_id is not None:
                try:
                    deck = Deck.objects.get(pk=deck_id)
                    redirect(reverse('core:deck-edit', args=[deck.id]))
                except ObjectDoesNotExist:
                    return redirect(reverse('core:index'))
            return redirect(reverse('core:index'))

    card_form = FlashCardForm()
    return render(request, "core/flash_card/create.html",
                  {"card_form": card_form})


def card_edit(request: HttpRequest, id: int):
    if request.method == "POST":
        card_form = FlashCardForm(request.POST, instance=FlashCard.objects.get(pk=id))
        if card_form.is_valid():
            print("saving card")
            card_form.save()
            return redirect(reverse('core:card-edit', args=[id]))

    print("loading card")
    card = get_object_or_404(FlashCard, pk=id)
    card_form = FlashCardForm(instance=card)
    return render(request, 'core/flash_card/edit.html', {"card_form": card_form})
