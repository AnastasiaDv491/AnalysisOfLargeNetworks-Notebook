from django.db import models
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,DateTimeFormatProperty,RelationshipFrom)


class Document(StructuredNode):
    doc_id = StringProperty(unique_index=True, required=True)
    type = StringProperty(unique_index=False, required=False)
    date = DateTimeFormatProperty(format = "%Y-%m-%d %H:%M:%S", required=False)
    year = IntegerProperty(unique_index=False, required=False)
    month = IntegerProperty(unique_index=False, required=False)
    day = IntegerProperty(unique_index=False, required=False)


class Article(StructuredNode):
    article_id = StringProperty(unique_index=True, required=True)
    title = StringProperty(unique_index=False, required=False)
    document = RelationshipFrom(Document, 'ARTICLE')


class ArticleVersion(StructuredNode):
    article_v_id = StringProperty(unique_index=True, required=True)
    title = StringProperty(unique_index=False, required=False)
    type = StringProperty(unique_index=False, required=False)
    start_date = DateTimeFormatProperty(format = "%Y-%m-%d %H:%M:%S", required=False)
    end_date = DateTimeFormatProperty(format = "%Y-%m-%d %H:%M:%S", required=False)

    article = RelationshipFrom(Article, 'VERSION')

class Date(StructuredNode):
    date_id = StringProperty(unique_index = True, required = True)
    date = DateTimeFormatProperty(format = "%Y-%m-%d", required=False)

    document_date = RelationshipFrom(Document, "CREATED_ON")

class Year(StructuredNode):
    year_id = StringProperty(unique_index = True, required = True)
    year = IntegerProperty(unique_index=False, required=False)

    document_year = RelationshipFrom(Document, "YEAR")

class Month(StructuredNode):
    month_id = StringProperty(unique_index = True, required = True)
    month = IntegerProperty(unique_index=False, required=False)

    document_month = RelationshipFrom(Document, "MONTH")

class Day(StructuredNode):
    day_id = StringProperty(unique_index = True, required = True)
    day = IntegerProperty(unique_index=False, required=False)

    document_day = RelationshipFrom(Document, "DAY")