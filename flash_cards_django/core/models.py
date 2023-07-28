from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(BaseModel):
    """Easy categorize your flashcards grouping them by tag"""
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)


class Deck(BaseModel):
    """Let's you organize your flashcards in groups for partial repetition"""
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title


class FlashCard(BaseModel):
    front = models.TextField(blank=False)
    back = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    decks = models.ManyToManyField(Deck)
    is_question = models.BooleanField(default=False)


class Hint(BaseModel):
    """Extra info for helping on repetition session"""
    content = models.TextField(blank=False)
    flash_card = models.ForeignKey(FlashCard, on_delete=models.CASCADE)


class PossibleChoice(BaseModel):
    content = models.TextField()
    flash_card = models.ForeignKey(FlashCard, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)


# class RepetitionDeck(BaseModel):
#     repetition_session = models.ForeignKey(
#         RepetitionSession, on_delete=models.CASCADE)
#     deck = models.ForeignKey(Deck, on_delete=models.CASCADE)


class TextAnswer(BaseModel):
    content = models.TextField()
    flash_card = models.ForeignKey(FlashCard, on_delete=models.CASCADE)


class DeckReviewedEvent(BaseModel):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)


class FlashCardReviewedEvent(BaseModel):
    flash_card = models.ForeignKey(FlashCard, on_delete=models.CASCADE)
