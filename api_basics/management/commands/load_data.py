from django.core.management import BaseCommand

from DRF.api_basics.models import Article


def is_title_already_exits(title):
    """
    :param name:
    :return:
    """
    try:
        title_id = Article.objects.get(title=title).id
        return title_id
    except:
        return None

def load_data_in_article(title, author, email, date):
    """



    """
    if is_title_already_exits(title):
        title_id = Article.objects.get(title=title).id
        return title_id

    temp_row = Article(title=title, author=author, email=email, date=date
                       )

    temp_row.save()

    title_id = Article.objects.get(title=title).id
    print("title_id : ", title_id)
    return title_id


class Command(BaseCommand):
    """
    command executor
    """
    help = 'Load CSV data into postgreSQL from seperate lenders.csv'
    def handle(self, *args, **kwargs):
        print("Handle Started")
        from datetime import date
        date = date.today()

        data = [["title1", "author1", "email1@gmail.com", date],
                ["title2", "author2", "email2@gmail.com", date],
                ["title3", "author3", "email3@gmail.com", date],
                ["title4", "author4", "email4@gmail.com", date]]

        for item in data:
            title_id = load_data_in_article(item[0], item[1], item[2], item[3])
            print(title_id)


