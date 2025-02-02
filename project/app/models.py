

from django.db import models
from ckeditor.fields import RichTextField

# Create FAQ model
class FAQ(models.Model):
    question = RichTextField()  # Use RichTextField for the question to support WYSIWYG editor
    answer = RichTextField()  # Answer with WYSIWYG editor

    # Language-specific fields
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation

    # Method to get translated question dynamically
    def get_translated_question(self, language_code):
        if language_code == 'hi' and self.question_hi:
            return self.question_hi
        elif language_code == 'bn' and self.question_bn:
            return self.question_bn
        else:
            return self.question  # Default language is English

    def __str__(self):
        return self.question
