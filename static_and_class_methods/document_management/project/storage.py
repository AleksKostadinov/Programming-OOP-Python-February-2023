from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = [category for category in self.categories if category.id == category_id][0]
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [topic for topic in self.topics if topic.id == topic_id][0]
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = [document for document in self.documents if document.id == document_id][0]
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = [category for category in self.categories if category.id == category_id][0]
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = [topic for topic in self.topics if topic.id == topic_id][0]
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = [document for document in self.documents if document.id == document_id][0]
        self.documents.remove(document)

    def get_document(self, document_id):
        return [document for document in self.documents if document.id == document_id][0]

    def __repr__(self):
        # return "\n".join(str(d) for d in self.documents)
        return '\n'.join(document.__repr__() for document in self.documents)

