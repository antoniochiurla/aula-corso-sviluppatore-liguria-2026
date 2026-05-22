import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Task } from '../models/task.model';

@Injectable({
  providedIn: 'root'
})
export class TaskService {
  private apiUrl = 'http://localhost:8000/api/';

  constructor(private http: HttpClient) { }

  getTasks(): Observable<Task[]> {
    return this.http.get<Task[]>(`${this.apiUrl}tasks/`);
  }

  addTask(task: any, type: string): Observable<any> {
    let endpoint = 'tasks/';
    if (type === 'bug') endpoint = 'bugs/';
    else if (type === 'feature') endpoint = 'features/';

    return this.http.post(`${this.apiUrl}${endpoint}`, task);
  }

  toggleTask(id: number): Observable<any> {
    return this.http.post(`${this.apiUrl}tasks/${id}/toggle/`, {});
  }

  deleteTask(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}tasks/${id}/`);
  }
}
