


class RegistrationForm(FlaskForm):
	username = StringField('Username', 
		                    validators=[DataRequired(), Length(min=2, max=20)])
		
	email = StringField('Email',
	                    validators=[DataRequired(), Email()])


	password = PasswordField('Password', 
		                    validators=[DataRequired()])

	confirm_password = PasswordField('Confirm Password', 
		                    validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Sorry, Username Taken. Please choose another name')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Sorry, email Taken, Please provide another email')



class UpdateAccountForm(FlaskForm):
	username = StringField('Username', 
		                    validators=[DataRequired(), Length(min=2, max=20)])
		
	email = StringField('Email',
	                    validators=[DataRequired(), Email()])

	picture = FileField('Update Profile Pic', validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('Sorry, Username Taken. Please choose another name')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Sorry, email Taken, Please provide another email')



class LoginForm(FlaskForm):
	username = StringField('Username', 
		                    validators=[DataRequired(), 
		                    Length(min=2, max=20)]) 

	email = StringField('Email',
	                    validators=[DataRequired(), Email()])


	password = PasswordField('Password', 
		                    validators=[DataRequired()])

	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')


class RequestResetForm(FlaskForm):
	email = StringField('Email',
	                    validators=[DataRequired(), Email()])

	submit = SubmitField('Request Password Reset')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError('There is No Account With That Email, You Must Register First')


class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password', 
		                    validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', 
		                    validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Reset Password')
