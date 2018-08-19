import os
import pandas as pd
from functools import partial

class Views:
	def view_menu(self):
		self.menu_grid.addWidget(self.u.UQtxt("MENU_STD_TITLE",title="Choisissez une action"))
		# self.menu_grid.addWidget(self.u.UQbut("MENU_STD_BUT",title="Import de fichier",connect2=["clicked",self.view_add_processing]))
		self.menu_grid.addWidget(self.u.UQbut("MENU_STD_BUT",title="Message automatique",connect2=["clicked",self.view_box_remote_msgs]))

	def view_add_processing(self):
		self.tools_remove_items(self.content_grid)
		self.content_grid.addWidget(self.u.UQtxt("BOX_STD_TITLE",title="Traitement fichier"))
		grid = self.design_sub_box(self.content_grid,1,1)
		grid.addWidget(self.u.UQtxt("SUBBOX_STD_TITLE",title="Nouveau fichier"))
		grid.addWidget(self.u.UQbut("STD_BUTTON",title="Choisir un fichier",connect2=["clicked",self.sig_file_open]))
	
	def view_box_remote_msgs(self):
		self.tools_remove_items(self.content_grid)
		self.content_grid.addWidget(self.u.UQtxt("BOX_STD_TITLE",title="Message automatique"),1)
		grid = self.design_sub_box(self.content_grid,1,1)
		grid.addWidget(self.u.UQtxt(style="label",title="Veuillez ajouter un fichier contact au format CSV ou txt (la première ligne doit contenir les titres de colonnes"),1,0,1,2);
		grid.addWidget(self.u.UQtxt(style="label", title="Choisissez le séparateur utiliser"),2,0)
		grid.addWidget(self.u.UQcombo(items=[';','espace',','],style="field"),2,1)
		grid.addWidget(self.u.UQbut("STD_BUTTON",title="Choisir un fichier",connect2=["clicked",self.sig_file_open]),3,0)
		grid.addWidget(self.u.UQtxt("SUBBOX_STD_TITLE",title="Nouveau fichier"),0,0,1,grid.columnCount())


	def view_open_file(self,fpath):
		self.tools_remove_item(self.content_grid,2)
		grid = self.design_sub_box(self.content_grid,2)
		ftitle = os.path.basename(fpath)
		self.current_file = fpath
		sep = self.content_grid.get_widget_by_pos(1).layout().get_widget_by_pos(2,1).currentText()
		if sep == 'espace': sep = " "
		data = pd.read_csv(fpath,sep,encoding="ISO-8859-1")
		cols = data.columns
		grid.addWidget(self.u.UQtxt(style="label",title="Colonnes telephone"),1,0)
		grid.addWidget(self.u.UQtxt(style="label",title="Colonne prénom"),1,1)
		w = self.u.UQwidget()
		g_tel = self.u.UQvboxlayout()
		grid.addWidget(w,2,0)
		w.setLayout(g_tel)
		w = self.u.UQwidget()
		grid.addWidget(w,2,1)
		g_prenom = self.u.UQvboxlayout()
		w.setLayout(g_prenom)
		grid.addWidget(self.u.UQtxt(style="line_h",title=""),3,0,1,grid.columnCount())
		grid.addWidget(self.u.UQtxt(style="label",title="Ajouter en début de message 'Bonjour' + prenom"),4,0)
		grid.addWidget(self.u.UQcheckbox(),4,1)
		for i in range(len(cols)):
			g_tel.addWidget(self.u.UQcheckbox(title=cols[i]),i)
			g_prenom.addWidget(self.u.UQcheckbox(exclusive=True,title=cols[i]),i)
		grid.addWidget(self.u.UQtxt(style="label",title='Message'),5,0)
		grid.addWidget(self.u.UQplaintxtedit(placeholder="Ecrivez votre message"),6,0,1,grid.columnCount())
		grid.addWidget(self.u.UQtxt("SUBBOX_STD_TITLE",title=ftitle),0,0,1,grid.columnCount())
		grid.addWidget(self.u.UQbut("STD_BUTTON",title="Lancer les messages",connect2=["clicked",partial(self.sig_process_data,data,grid)]),7,0)
		grid.addWidget(self.u.UQbut("STD_BUTTON",title="Configure position souris",connect2=["clicked",self.sig_configure_pointer,data,grid]),7,1)


				

