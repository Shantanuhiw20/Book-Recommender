from flask import Flask, render_template, request
import numpy as np
import pickle

popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_score = pickle.load(open('similarity_score.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=popular_df['Book-Title'].values,
                           author=popular_df['Book-Author'].values,
                           image=popular_df['Image-URL-M'].values,
                           rating=popular_df['avg_ratings'].values,
                           votes=popular_df['num_ratings'].values)

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommended_books', methods=['POST'])
def recommend_books():
    user_input = request.form.get('user_input').strip()

    # If the book isn't in your pivot table index, show an error
    if user_input not in pt.index:
        return render_template(
            'recommend.html',
            error=True,
            user_input=user_input,
            data=[]
        )

    # Otherwise proceed as before
    idx = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(
        enumerate(similarity_score[idx]),
        key=lambda x: x[1],
        reverse=True
    )[1:7]  # top 6

    data = []
    for i, _ in similar_items:
        temp = books[books['Book-Title'] == pt.index[i]]
        title = temp.drop_duplicates('Book-Title')['Book-Title'].values[0]
        author = temp.drop_duplicates('Book-Title')['Book-Author'].values[0]
        img   = temp.drop_duplicates('Book-Title')['Image-URL-M'].values[0]
        data.append([title, author, img])

    return render_template(
        'recommend.html',
        data=data,
        user_input=user_input,
        error=False
    )

if __name__ == '__main__':
    app.run(debug=True)

