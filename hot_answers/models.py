from django.db import models


# Create your models here.
class Answers(models.Model):
    """Model for Zhihu hot answers."""
    answer_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=300)
    question_link = models.URLField(unique=True)
    author = models.CharField(max_length=200)
    author_link = models.URLField(blank=True)
    vote = models.PositiveIntegerField()
    summary_img = models.TextField(blank=True)
    summary_text = models.TextField()
    answer = models.TextField()
    date = models.DateField()

    class Meta:
        """ Use the data table created and updated by zhihu_scraper. """
        managed = False
        db_table = 'answers'

        verbose_name_plural = "Answers"

    def __unicode__(self):
        """Use question as representation of Answer object."""
        return self.question
