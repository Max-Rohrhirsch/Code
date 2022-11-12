////////////////////////////
// INCLUDE
////////////////////////////

#include <wx/wx.h>


////////////////////////////
// FRAME
////////////////////////////

class MyFrame : public wxFrame {
    public:
        MyFrame(const wxString& title)
    		:wxFrame(NULL, wxID_ANY, title, wxDefaultPosition, wxSize(250, 150))
    	{
    		Centre();
    	}
};


////////////////////////////
// APP
////////////////////////////

class MyApp : public wxApp {
    public:
    	bool OnInit()
    	{
    		MyFrame *frame1 = new MyFrame(wxT("Frame 1"));
    		frame1 -> Show(true);
    		return true;
    	}
};

////////////////////////////
// RUN
////////////////////////////

wxIMPLEMENT_APP(MyApp);


////////////////////////////
// OPTIONS
////////////////////////////

wxMenu *menuFile = new wxMenu;
menuFile->Append(ID_Hello, "&Hello...\tCtrl-H",
                 "Help string shown in status bar for this menu item");
menuFile->AppendSeparator();
menuFile->Append(wxID_EXIT);

wxMenu *menuHelp = new wxMenu;
menuHelp->Append(wxID_ABOUT);

wxMenuBar *menuBar = new wxMenuBar;
menuBar->Append(menuFile, "&File");
menuBar->Append(menuHelp, "&Help");

SetMenuBar(menuBar);

CreateStatusBar();
SetStatusText("Welcome to wxWidgets!");


////////////////////////////
// BINDS + ...
////////////////////////////

Bind(wxEVT_MENU, &MyFrame::OnHello, this, ID_Hello);
Bind(wxEVT_MENU, &MyFrame::OnAbout, this, wxID_ABOUT);
Bind(wxEVT_MENU, &MyFrame::OnExit, this, wxID_EXIT);


void MyFrame::OnExit(wxCommandEvent& event)
{
    Close(true);
}


 wxLogMessage("Hello world from wxWidgets!");


////////////////////////////
// DRAW
////////////////////////////
void 	DrawCircle (wxCoord x, wxCoord y, wxCoord radius)
void 	DrawCircle (const wxPoint &pt, wxCoord radius)

void 	DrawEllipse (wxCoord x, wxCoord y, wxCoord width, wxCoord height)

void 	DrawIcon (const wxIcon &icon, const wxPoint &pt)

void 	DrawLabel (const wxString &text, const wxBitmap &bitmap, const wxRect &rect, int alignment=wxALIGN_LEFT|wxALIGN_TOP, int indexAccel=-1, wxRect *rectBounding=NULL)

void 	DrawLine (wxCoord x1, wxCoord y1, wxCoord x2, wxCoord y2)
void 	DrawLine (const wxPoint &pt1, const wxPoint &pt2)

void 	DrawPoint (wxCoord x, wxCoord y)
void 	DrawPoint (const wxPoint &pt)

void    DrawRectangle (wxCoord x, wxCoord y, wxCoord width, wxCoord height)

////////////////////////////
// TUTORIAL
////////////////////////////























//
