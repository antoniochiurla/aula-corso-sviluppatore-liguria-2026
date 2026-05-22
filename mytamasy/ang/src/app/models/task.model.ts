export interface Task {
  id?: number;
  title: string;
  description: string;
  created_at?: string;
  created_by?: number;
  created_by_username?: string;
  status: 'AP' | 'CL';
  task_type?: 'base' | 'bug' | 'feature';
  severity?: string;
  priority?: string;
}
