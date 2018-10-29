




class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	content = TextAreaField('content', validators=[DataRequired()])
	submit = SubmitField('Post')