import { Component, OnInit } from '@angular/core';
import { TaskService } from './services/task.service';
import { Task } from './models/task.model';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  tasks: Task[] = [];
  newTaskTitle = '';
  newTaskDesc = '';
  newTaskType = 'base';

  constructor(private taskService: TaskService) {}

  ngOnInit() {
    this.loadTasks();
  }

  loadTasks() {
    this.taskService.getTasks().subscribe(tasks => {
      this.tasks = tasks;
    });
  }

  addTask() {
    if (!this.newTaskTitle) return;

    const taskData: any = {
      title: this.newTaskTitle,
      description: this.newTaskDesc,
      status: 'AP'
    };

    if (this.newTaskType === 'bug') {
      taskData.severity = 'ME';
    } else if (this.newTaskType === 'feature') {
      taskData.priority = '2';
    }

    this.taskService.addTask(taskData, this.newTaskType).subscribe(() => {
      this.newTaskTitle = '';
      this.newTaskDesc = '';
      this.loadTasks();
    });
  }

  toggleTask(id: number | undefined) {
    if (id === undefined) return;
    this.taskService.toggleTask(id).subscribe(() => {
      this.loadTasks();
    });
  }

  deleteTask(id: number | undefined) {
    if (id === undefined) return;
    if (confirm('Sicuro di voler eliminare questo task?')) {
      this.taskService.deleteTask(id).subscribe(() => {
        this.loadTasks();
      });
    }
  }
}
