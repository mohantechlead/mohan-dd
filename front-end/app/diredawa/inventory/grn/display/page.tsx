import { columns, Payment } from "./columns"
import { DataTable } from "@/components/data-table"

async function getData(): Promise<Payment[]> {
    
    const grns = await fetch('http://127.0.0.1:8000/api/inventory') 
    const data = await grns.json();
    return data;      
    
}

export default async function DemoPage() {
  const data = await getData()

  return (
    <div className="container mx-auto py-10">
      <DataTable columns={columns} data={data} />
    </div>
  )
}