<?php

use App\Http\Controllers\StudentController;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Route::get('students/', [StudentController::class, 'index'])->name('students.index');
Route::get('students/{student}/show', [StudentController::class, 'show'])->name('students.show');
Route::get('students/create', [StudentController::class, 'create'])->name('students.create');
Route::post('students', [StudentController::class, 'store'])->name('students.store');
Route::get('students/{student}/edit', [StudentController::class, 'edit'])->name('students.edit');
Route::put('students/{student}', [StudentController::class, 'update'])->name('students.update');
Route::delete('students/{student}', [StudentController::class, 'destroy'])->name('students.destroy');