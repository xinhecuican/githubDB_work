import React,{Component} from 'react'
import './Footer.css'

export default class Footer extends Component{

    // 全选的回调
    handleCheckAll = (event)=>{
        this.props.checkAllTodo(event.target.checked)
    }

    // 清除所有已完成的回调
    handleClearAll = ()=>{
        this.props.clearAllDone()
    }
    
    render(){
        const {todos} = this.props
        // 已完成的个数
        const doneCount = todos.reduce((pre,todo)=>{
            return pre+(todo.done?1:0)
        },0) // 0是pre的值
        // 总数
        const total = todos.length
        return (
            <div className="todo-footer">
                <label>
                    <input type="checkbox" onChange={this.handleCheckAll} checked={doneCount === total && total !== 0?true:false}/>
                </label>
                <span>
                    <span>已完成{doneCount}</span> / 全部{total}
                </span>
                <button onClick={this.handleClearAll} className="btn btn-danger">清除已完成任务</button>
            </div>
        )
    }
}