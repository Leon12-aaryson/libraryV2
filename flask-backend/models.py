from exts import db

"""
class Book:
  id:int primary_key
  title:str
  author:str
  description:str (text)
"""

class Books(db.Model):
  id=db.Column(db.Integer(),primary_key=True)
  title=db.Column(db.String(), nullable=False)
  author=db.Column(db.Text(),nullable=False)
  description=db.Column(db.Text(),nullable=False)
  
  def __repr__(self):
    return f"<Book {self.title}>"
  
  def save(self):
    db.session.add(self)
    db.session.commit()
  
  def delete(self):
    db.session.delete(self)
    db.session.commit()
    
  def update(self,title,author,description):
    self.title=title
    self.author=author
    self.description=description
