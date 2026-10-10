import customtkinter as ctk

from gui import theme
from gui.home import HomePage
from gui.student_form import StudentFormPage
from gui.results import ResultsPage
from gui.colleges import CollegesPage
from gui.guide import GuidePage
from gui.about import AboutPage
from gui.cutoff import CutoffPage


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


class TNEAApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("TNEA Student Guide")
        self.geometry("1280x760")
        self.minsize(1080, 640)
        self.configure(fg_color=theme.BG)

        self.current_page = None

        self.show_home()

    # ======================================================
    # PAGE SWAPPING
    # ======================================================

    def clear_page(self):

        if self.current_page is not None:
            self.current_page.destroy()

        self.current_page = None

    def _set_page(self, page):

        self.clear_page()

        self.current_page = page

        self.current_page.pack(
            fill="both",
            expand=True
        )

    def show_home(self):
        self._set_page(
            HomePage(
                self,
                self.show_student_form,
                self.show_colleges,
                self.show_guide,
                self.show_cutoff,
                self.show_about
            )
        )

    def show_student_form(self):
        self._set_page(
            StudentFormPage(
                self,
                self.show_home,
                self.show_results
            )
        )

    def show_results(self, results):
        self._set_page(
            ResultsPage(
                self,
                results,
                self.show_student_form
            )
        )

    def show_colleges(self):
        self._set_page(
            CollegesPage(
                self,
                self.show_home
            )
        )

    def show_guide(self):
        self._set_page(
            GuidePage(
                self,
                self.show_home
            )
        )

    def show_cutoff(self):
        self._set_page(
            CutoffPage(
                self,
                self.show_home
            )
        )

    def show_about(self):
        self._set_page(
            AboutPage(
                self,
                self.show_home
            )
        )


if __name__ == "__main__":

    app = TNEAApp()

    app.mainloop()
