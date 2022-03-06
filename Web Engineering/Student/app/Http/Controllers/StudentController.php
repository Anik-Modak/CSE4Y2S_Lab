<?php

namespace App\Http\Controllers;
use App\Models\Student;
use Illuminate\Http\Request;

class StudentController extends Controller
{
    public function index(Request $request)
    {
        if ($request->has('search')) {
            $students = Student::where('name', 'like', '%' . $request->get('search') . '%')
                ->orWhere('dept', 'like', '%' . $request->get('search') . '%')
                ->paginate(10);
        } else {
            $students = Student::paginate(10);
        }

        return view('students.index', ['students' => $students]);
    }

    public function show(Request $request, Student $student)
    {
        return view('students.show', ['student' => $student]);
    }

    public function create()
    {
        return view('students.create');
    }

    public function store(Request $request)
    {
        $request->validate([
            'name'  => 'required|max:255',
            'dept'   => 'required|max:25',
            'address' => 'required|max:255',
            'phone'  => 'required|max:11',
        ]);

        Student::create($request->all());

        return redirect()->route('students.index');

    }

    public function edit(Request $request, $id)
    {
        $student = Student::find($id);

        return view('students.edit', ['student' => $student]);
    }

    public function update(Request $request, $id)
    {
        $request->validate([
            'name'  => 'required|max:255',
            'dept'   => 'required|max:25',
            'address' => 'required|max:255',
            'phone'  => 'required|max:11',
        ]);

        $student = Student::find($id);
        $student->update($request->all());

        return redirect()->route('students.index');
    }

    public function destroy(Request $request, $id)
    {
        $student = Student::find($id);
        $student->delete();

        return redirect()->route('students.index');
    }

}

