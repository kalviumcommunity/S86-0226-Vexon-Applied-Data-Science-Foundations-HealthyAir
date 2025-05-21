const mongoose = require('mongoose');
const tasks = require('./schema');
const router = require('Router');

Router post('./add', async (req, res)=>{
    const newTasks = newTasks (req.body);
    await newTasks.save();
    res.status(201).json(newTasks); {

    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

Router get('./', async (req, res) => {
    const Tasks = await Tasks.find();
    res.status(200).json(Tasks); {

    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

module.router = export(Tasks);