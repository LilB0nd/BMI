# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Panel
###########################################################################

class Panel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 340,240 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetMinSize( wx.Size( 340,240 ) )
		self.SetMaxSize( wx.Size( 340,240 ) )

		main_sizer = wx.BoxSizer( wx.VERTICAL )

		input_sizer = wx.BoxSizer( wx.HORIZONTAL )

		Geschlecht = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Geschlecht" ), wx.VERTICAL )

		self.male_button = wx.RadioButton( Geschlecht.GetStaticBox(), wx.ID_ANY, u"männlich", wx.DefaultPosition, wx.DefaultSize, 0 )
		Geschlecht.Add( self.male_button, 1, wx.ALL, 5 )

		self.female_button = wx.RadioButton( Geschlecht.GetStaticBox(), wx.ID_ANY, u"weiblich", wx.DefaultPosition, wx.DefaultSize, 0 )
		Geschlecht.Add( self.female_button, 1, wx.ALL, 5 )

		self.divers_button = wx.RadioButton( Geschlecht.GetStaticBox(), wx.ID_ANY, u"divers", wx.DefaultPosition, wx.DefaultSize, 0 )
		Geschlecht.Add( self.divers_button, 0, wx.ALL, 5 )


		input_sizer.Add( Geschlecht, 0, wx.EXPAND, 5 )

		Personen_sizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Personendaten" ), wx.HORIZONTAL )

		groesse_sizer = wx.BoxSizer( wx.VERTICAL )

		self.text_groesse = wx.StaticText( Personen_sizer.GetStaticBox(), wx.ID_ANY, u"Größe:", wx.DefaultPosition, wx.Size( 60,20 ), wx.ALIGN_RIGHT )
		self.text_groesse.Wrap( -1 )

		groesse_sizer.Add( self.text_groesse, 0, wx.ALIGN_CENTER|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.text_gewicht = wx.StaticText( Personen_sizer.GetStaticBox(), wx.ID_ANY, u"Gewicht:", wx.DefaultPosition, wx.Size( 60,20 ), wx.ALIGN_RIGHT )
		self.text_gewicht.Wrap( -1 )

		groesse_sizer.Add( self.text_gewicht, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.text_alter = wx.StaticText( Personen_sizer.GetStaticBox(), wx.ID_ANY, u"Alter: ", wx.DefaultPosition, wx.Size( 60,20 ), wx.ALIGN_RIGHT )
		self.text_alter.Wrap( -1 )

		groesse_sizer.Add( self.text_alter, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		Personen_sizer.Add( groesse_sizer, 0, wx.EXPAND, 5 )

		gewicht_sizer = wx.BoxSizer( wx.VERTICAL )

		self.input_size = wx.TextCtrl( Personen_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		gewicht_sizer.Add( self.input_size, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.input_weight = wx.TextCtrl( Personen_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		gewicht_sizer.Add( self.input_weight, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.input_age = wx.TextCtrl( Personen_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		gewicht_sizer.Add( self.input_age, 1, wx.ALL, 5 )


		Personen_sizer.Add( gewicht_sizer, 0, 0, 5 )

		alter_sizer = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText121 = wx.StaticText( Personen_sizer.GetStaticBox(), wx.ID_ANY, u"cm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )

		self.m_staticText121.SetMinSize( wx.Size( 60,20 ) )
		self.m_staticText121.SetMaxSize( wx.Size( 60,20 ) )

		alter_sizer.Add( self.m_staticText121, 1, wx.ALIGN_LEFT|wx.ALL, 5 )

		self.m_staticText131 = wx.StaticText( Personen_sizer.GetStaticBox(), wx.ID_ANY, u"kg", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )

		self.m_staticText131.SetMinSize( wx.Size( 60,20 ) )
		self.m_staticText131.SetMaxSize( wx.Size( 60,20 ) )

		alter_sizer.Add( self.m_staticText131, 0, wx.ALIGN_CENTER|wx.ALIGN_LEFT|wx.ALL, 5 )


		alter_sizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		Personen_sizer.Add( alter_sizer, 0, wx.EXPAND, 5 )


		input_sizer.Add( Personen_sizer, 1, wx.EXPAND, 5 )


		main_sizer.Add( input_sizer, 1, wx.EXPAND, 5 )

		output_sizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Ergebnis" ), wx.VERTICAL )

		bewertung_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.text_bewertung = wx.StaticText( output_sizer.GetStaticBox(), wx.ID_ANY, u"Bewertung:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.text_bewertung.Wrap( -1 )

		bewertung_sizer.Add( self.text_bewertung, 0, wx.ALL, 5 )

		self.output_raiting = wx.StaticText( output_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_SUNKEN )
		self.output_raiting.SetLabelMarkup( wx.EmptyString )
		self.output_raiting.Wrap( -1 )

		self.output_raiting.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.output_raiting.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		self.output_raiting.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bewertung_sizer.Add( self.output_raiting, 1, wx.ALL, 5 )


		output_sizer.Add( bewertung_sizer, 0, wx.EXPAND, 5 )

		output_sizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.text_BMI = wx.StaticText( output_sizer.GetStaticBox(), wx.ID_ANY, u"BMI:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.text_BMI.Wrap( -1 )

		output_sizer2.Add( self.text_BMI, 0, wx.ALL, 5 )

		self.output_BMI = wx.StaticText( output_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_SUNKEN )
		self.output_BMI.Wrap( -1 )

		output_sizer2.Add( self.output_BMI, 1, wx.ALL, 5 )

		self.text_idealweight = wx.StaticText( output_sizer.GetStaticBox(), wx.ID_ANY, u"Idealgewicht:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.text_idealweight.Wrap( -1 )

		output_sizer2.Add( self.text_idealweight, 0, wx.ALL, 5 )

		self.output_idealweight = wx.StaticText( output_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_SUNKEN )
		self.output_idealweight.Wrap( -1 )

		output_sizer2.Add( self.output_idealweight, 1, wx.ALL, 5 )

		self.text_idealweight_unit = wx.StaticText( output_sizer.GetStaticBox(), wx.ID_ANY, u"kg", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.text_idealweight_unit.Wrap( -1 )

		output_sizer2.Add( self.text_idealweight_unit, 0, wx.ALL, 5 )


		output_sizer.Add( output_sizer2, 0, wx.EXPAND, 5 )


		main_sizer.Add( output_sizer, 0, wx.EXPAND, 5 )

		botton_sizer = wx.BoxSizer( wx.HORIZONTAL )


		botton_sizer.Add( ( 0, 0), 2, wx.EXPAND, 5 )

		self.button_exit = wx.Button( self, wx.ID_ANY, u"Beenden", wx.DefaultPosition, wx.DefaultSize, 0 )
		botton_sizer.Add( self.button_exit, 1, wx.ALIGN_RIGHT|wx.RIGHT, 5 )

		self.button_clac = wx.Button( self, wx.ID_ANY, u"Berechnen", wx.DefaultPosition, wx.DefaultSize, 0 )
		botton_sizer.Add( self.button_clac, 1, wx.ALIGN_RIGHT|wx.RIGHT, 5 )


		main_sizer.Add( botton_sizer, 0, wx.ALIGN_RIGHT|wx.EXPAND, 5 )


		self.SetSizer( main_sizer )
		self.Layout()

		# Connect Events
		self.button_exit.Bind( wx.EVT_BUTTON, self.click_exit )
		self.button_clac.Bind( wx.EVT_BUTTON, self.click_calc )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def click_exit( self, event ):
		event.Skip()

	def click_calc( self, event ):
		event.Skip()


