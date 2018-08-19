import pynput.mouse as pymouse
import pynput.keyboard as pykeyboard

class Tools:
	def tools_err_manage(self,*args,**kwargs):
		params = kwargs.get("params",None)
		vout = kwargs.get("vout",None)
		if len(args) == 0: return 0
		listargs = args
		if isinstance(listargs[0],list): listargs = listargs[0]
		err_num = listargs[0]
		if len(listargs) == 2 and params is None: params = listargs[1]
		if len(listargs) == 3 and vout is None: vout = listargs[2]
		if err_num >= 0x0001:
			self.u.UQapplication.restoreOverrideCursor()
			if self.errors[err_num]["group"] in self.u.utxt:
				group = self.u.utxt[self.errors[err_num]["group"]][self.u.ulang]
			else: group = self.errors[err_num]["group"]
			if self.errors[err_num]["msg"] in self.u.utxt:
				msg = self.u.utxt[self.errors[err_num]["msg"]][self.u.ulang]
			else: msg = self.errors[err_num]["msg"]
			msg = '0x{:04x}'.format(err_num) + " : " +msg
			if vout == "c":
				if params is not None:
					print(group,"Items"+ " : " + params + "\n" + msg)
				else:
					print(group,msg)
			else:
				if params is not None:
					self.u.txtBox(group,"Items"+ " : " + params + "\n" + msg,"critical")
				else:
					self.u.txtBox(group,msg,"critical")
		return err_num

	def tools_load_view(self,menu_id,content_id):
		self.menu_view = menu_id
		self.content_view = content_id

	def tools_remove_items(self,layout):
		if layout is not None:
		    for cnt in reversed(range(layout.count())):
		        w = layout.takeAt(cnt).widget()
		        if w is not None: 
		            w.deleteLater()

	def tools_remove_item(self,layGrid=None,line=None,col=None,widname=None):
		"""
			Suppression d'élément
		"""
		if widname is not None:
			wid = layGrid.get_child_by_name(widname)
			if wid is not None: wid.deleteLater()
			if layGrid.get_child_by_name(widname) is not None:
				wid.setParent(None)
		else:
			if layGrid.get_widget_by_pos(line,col) is not None:
				layGrid.get_widget_by_pos(line,col).deleteLater()
			if layGrid.get_widget_by_pos(line,col) is not None:
				layGrid.get_widget_by_pos(line,col).setParent(None)


	def tools_load_lang(self):
		bdd_lang = self.bdd_curs.select("Configuration","val",u_where="name='LANG_CHOOSE'")[0]
		if int(bdd_lang) == 0: self.u.ulang = "fr"
		else: self.u.ulang = "en"

	def tools_type_str(self,word):
		mouse = pymouse.Controller()
		keyboard = pykeyboard.Controller()
		for i in word:
			print(i)
			if i == '\n':
				keyboard.press(pykeyboard.Key.enter)
				keyboard.release(pykeyboard.Key.enter)
			else:
				keyboard.press(str(i))
				keyboard.release(str(i))
